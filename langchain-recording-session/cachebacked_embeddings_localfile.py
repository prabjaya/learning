# Local Embedding Cache Example
import os
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Create local cache folder (if not exists)
cache_folder = "./embeddings_cache"
os.makedirs(cache_folder, exist_ok=True)

# Underlying HF model (Here: MiniLM as an example)
underlying = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Local file storage backend
store = LocalFileStore(cache_folder)

# Wrap in Cache
cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings=underlying,
    document_embedding_cache=store,
    namespace=underlying.model_name,
)

# Test texts
docs = ["Hello world!", "How are you?"]

print("\n--- First Call: Will compute & cache ---")
emb1 = cached_embedder.embed_documents(docs)

print("\n--- Second Call: Instant from cache ---")
emb2 = cached_embedder.embed_documents(docs)

# show first 5 values for clarity
print("\nEmbedding sample:", emb1[0][:5])
print("Cache loaded sample:", emb2[0][:5])
