import time
# Install requirements:
# pip install langchain==0.2.10 langchain-community==0.2.9 sentence-transformers

from langchain.storage import InMemoryStore
from langchain.embeddings import CacheBackedEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Underlying embedding model (MiniLM)
underlying = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# In-memory cache (removed when program ends)
store = InMemoryStore()

# Wrap with caching
cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings=underlying,
    document_embedding_cache=store,
    namespace=underlying.model_name,
)

docs = ["Hello world", "How are you?"]

print("\n--- First Call: generates + caches ---")
start = time.time()
emb1 = cached_embedder.embed_documents(docs)
print("Time taken:", round(time.time() - start, 4), "seconds")
print("Sample:", emb1[0][:5])



print("\n--- Second Call: loads from cache ---")
start = time.time()
emb2 = cached_embedder.embed_documents(docs)
print("Time taken:", round(time.time() - start, 4), "seconds")
print("Sample:", emb2[0][:5])
