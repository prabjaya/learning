# Install dependencies if not already installed
# pip install langchain huggingface-hub
# Go to https://huggingface.co/ ---->create HUGGINGFACEHUB_API_TOKEN

import os
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_key:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN  is not found in .env file")

# Initialize the embedding model
model_name = "intfloat/multilingual-e5-large-instruct"
hf_embeddings = HuggingFaceEndpointEmbeddings(
    model=model_name,
    task="feature-extraction",
    huggingfacehub_api_token=api_key
)

# Sample texts
texts = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
]

# Embed documents
embedded_documents = hf_embeddings.embed_documents(texts)
print("[Document Embeddings]")
print(f"Model: {model_name}")
print(f"First embedding vector: {embedded_documents[0][:5]} ...") 

# Embed a single query
query = "Tell me about LangChain."
embedded_query = hf_embeddings.embed_query(query)
print("\n[Query Embedding]")
print(f"Query: {query}")
print(f"Embedding vector (first 10 values): {embedded_query[:10]} ...")
