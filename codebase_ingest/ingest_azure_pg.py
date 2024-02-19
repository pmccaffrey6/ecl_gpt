from llama_index.llms import AzureOpenAI
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.vector_stores import PGVectorStore
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
import logging
import sys

from sqlalchemy import make_url
import psycopg2

import os
os.environ['CURL_CA_BUNDLE'] = ''

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

from llama_index import set_global_service_context
from llama_index.extractors import (
    TitleExtractor,
    EntityExtractor,
)
#from llama_index.text_splitter import TokenTextSplitter
from llama_index.node_parser import SentenceSplitter
from llama_index.ingestion import IngestionPipeline, IngestionCache


text_splitter = SentenceSplitter(
    separator=" ", chunk_size=1024, chunk_overlap=128
)

title_extractor = TitleExtractor(nodes=5, llm=llm)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    transformations=[text_splitter, title_extractor]
)

set_global_service_context(service_context)

#documents = SimpleDirectoryReader(
#    input_files=["../vector_generator/example_text/documents_dir/elisa_sop.txt"]
#).load_data()
documents = SimpleDirectoryReader("../source_docs/ingest_dir/").load_data()
#index = VectorStoreIndex.from_documents(documents)

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

print(nodes)


###
#
###
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

vector_store.add(nodes)