from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
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
# Connect Qdrant client
# ----------------------------
client = QdrantClient(url=QDRANT_URL)

# ----------------------------
# Load Existing Collection into LangChain Qdrant wrapper
# ----------------------------
vector_store = Qdrant(
    client=client,
    collection_name=COLLECTION_NAME,
    embeddings=embeddings, # Pass the whole object here
)

# ----------------------------
# Perform Similarity Search
# ----------------------------
query = "Looking for a Python ML engineer"
results = vector_store.similarity_search(query, k=2)

# ----------------------------
# Print Results
# ----------------------------
print(f"Found {len(results)} results:")
for i, doc in enumerate(results, start=1):
    print(f"Result {i}: {doc.page_content}")