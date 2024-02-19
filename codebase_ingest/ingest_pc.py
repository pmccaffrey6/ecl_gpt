import logging
import sys
import os

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from pinecone import Pinecone, ServerlessSpec

os.environ["PINECONE_API_KEY"] = "45d47f59-4d01-4a2c-9a03-962ab97d8d6b"
os.environ['OPENAI_API_KEY'] = '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'

api_key = os.environ["PINECONE_API_KEY"]

pc = Pinecone(api_key=api_key)

# pc.create_index(
#     name="ecl-docs",
#     dimension=1536,
#     metric="euclidean",
#     spec=ServerlessSpec(cloud="aws", region="us-west-2")
# )
pinecone_index = pc.Index("ecl-docs")


from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore
from IPython.display import Markdown, display

documents = SimpleDirectoryReader("../source_docs/").load_data()

from llama_index.storage.storage_context import StorageContext

if "OPENAI_API_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable OPENAI_API_KEY is not set")

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)