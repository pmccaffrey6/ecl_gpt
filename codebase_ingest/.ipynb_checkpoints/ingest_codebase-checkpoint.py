from llama_index.llms import AzureOpenAI
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.vector_stores import PGVectorStore
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.storage.storage_context import StorageContext
from llama_index import set_global_service_context
from llama_index.extractors import (
    TitleExtractor,
    EntityExtractor,
)
#from llama_index.text_splitter import TokenTextSplitter
from llama_index.node_parser import SentenceSplitter
from llama_index.ingestion import IngestionPipeline, IngestionCache
from llama_index.vector_stores import PineconeVectorStore

import logging
import sys

import configparser
config = configparser.ConfigParser()
config.read('../configs/config.ini')

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO
)  # logging.DEBUG for more verbose output
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

api_key = config['AZUREOPENAI']['API_KEY']
azure_endpoint = config['AZUREOPENAI']['ENDPOINT']
api_version = "2023-07-01-preview"

import os
os.environ['CURL_CA_BUNDLE'] = ''






llm = AzureOpenAI(
    model=config['AZUREOPENAI']['LLM_MODEL'],
    deployment_name=config['AZUREOPENAI']['LLM_DEPLOYMENT_NAME'],
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

# You need to deploy your own embedding model as well as your own chat completion model
embed_model = AzureOpenAIEmbedding(
    model=config['AZUREOPENAI']['EMBEDDING_MODEL'],
    deployment_name=config['AZUREOPENAI']['EMBEDDING_DEPLOYMENT_NAME'],
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)




documents = SimpleDirectoryReader("../source_docs/").load_data()


text_splitter = SentenceSplitter(
    separator=" ", chunk_size=2048, chunk_overlap=128
)

title_extractor = TitleExtractor(nodes=5, llm=llm)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    transformations=[text_splitter, title_extractor]
)

set_global_service_context(service_context)

pipeline = IngestionPipeline(
    transformations=[text_splitter, title_extractor]
)

nodes = pipeline.run(
    documents=documents,
    show_progress=True
)

for node in nodes:
    node_embedding = embed_model.get_text_embedding(
        node.get_content(metadata_mode="all")
    )
    node.embedding = node_embedding

print("UPLOADING TO VECTORSTORE")





###
#
###
from pinecone import Pinecone, ServerlessSpec

api_key = config["VECTORSTORE"]["PINECONE_API_KEY"]
pc = Pinecone(api_key=api_key)

# pc.create_index(
#     name="quickstart",
#     dimension=1536,
#     metric="euclidean",
#     spec=ServerlessSpec(cloud="aws", region="us-west-2"),
# )

pinecone_index = pc.Index("ecl-docs")


vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

vector_store.add(nodes)