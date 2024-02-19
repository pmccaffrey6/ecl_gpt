import os

from llama_index.query_engine.retriever_query_engine import RetrieverQueryEngine
from llama_index.llms import AzureOpenAI
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.vector_stores import PGVectorStore
from llama_index import VectorStoreIndex, Document
from llama_index.callbacks.base import CallbackManager
from llama_index import set_global_service_context
from llama_index import (
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
import configparser
config = configparser.ConfigParser()
config.read('../configs/config.ini')
import psycopg2
from sqlalchemy import make_url

import chainlit as cl

@cl.on_chat_start
async def factory():
    llm_predictor = LLMPredictor(
        llm=AzureOpenAI(
            model=config['AZUREOPENAI']['LLM_MODEL'],
            deployment_name=config['AZUREOPENAI']['LLM_DEPLOYMENT_NAME'],
            api_key=config['AZUREOPENAI']['API_KEY'],
            azure_endpoint=config['AZUREOPENAI']['ENDPOINT'],
            api_version="2023-07-01-preview",
            streaming=True
        ),
        
    )

    embed_model = AzureOpenAIEmbedding(
        model=config['AZUREOPENAI']['EMBEDDING_MODEL'],
        deployment_name=config['AZUREOPENAI']['EMBEDDING_DEPLOYMENT_NAME'],
        api_key=config['AZUREOPENAI']['API_KEY'],
        azure_endpoint=config['AZUREOPENAI']['ENDPOINT'],
        api_version="2023-07-01-preview"
    )

    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        chunk_size=512,
        embed_model=embed_model,
        callback_manager=CallbackManager([cl.LlamaIndexCallbackHandler()]),
    )
    set_global_service_context(service_context)

    connection_string = config['VECTORSTORE']['CONNECTION_STRING']
    db_name = config['VECTORSTORE']['DB_NAME']
    conn = psycopg2.connect(connection_string)
    conn.autocommit = True

    url = make_url(connection_string)
    vector_store = PGVectorStore.from_params(
        database=db_name,
        host=url.host,
        password=url.password,
        port=url.port,
        user=url.username,
        table_name="ecl_docs",
        embed_dim=1536,  # openai embedding dimension
    )

    index = VectorStoreIndex.from_vector_store(vector_store)
    #index.storage_context.persist()

    query_engine = index.as_query_engine(
        service_context=service_context,
        streaming=True
    )

    cl.user_session.set("query_engine", query_engine)




@cl.on_message
async def main(message: cl.Message):
    query_engine = cl.user_session.get("query_engine")  # type: RetrieverQueryEngine
    response = await cl.make_async(query_engine.query)(message.content)

    response_message = cl.Message(content="")

    for token in response.response_gen:
        await response_message.stream_token(token=token)

    if response.response_txt:
        response_message.content = response.response_txt

    await response_message.send()