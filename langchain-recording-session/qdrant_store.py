# run the qdrant in local
# docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
# another terminal run this file to create collection and store vectors
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document  
from qdrant_client import QdrantClient

# ----------------------------
# CONFIG
# ----------------------------
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "collection_new"

# ----------------------------
# Embedding Model
# ----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------
# Sample Documents
# ----------------------------
docs = [
    Document(page_content="Python developer with machine learning experience"),
    Document(page_content="Java backend engineer with Spring Boot expertise"),
    Document(page_content="Data scientist skilled in NLP and deep learning"),
]

# ----------------------------
# Create Qdrant Client
# ----------------------------
client = QdrantClient(url=QDRANT_URL)

# ----------------------------
# Create Collection + Store Vectors
# ----------------------------
# Note: In newer versions, consider using QdrantVectorStore or similar classes,
# but this method still works for basic setups if langchain-community is installed.
vector_store = Qdrant.from_documents(
    documents=docs,
    embedding=embeddings,
    client=client,
    collection_name=COLLECTION_NAME,
)

print("✅ Embeddings stored in Qdrant")