from dotenv import load_dotenv
from langchain_upstage import UpstageEmbeddings

# 1. Load your API key from .env (UPSTAGE_API_KEY=up_...)
load_dotenv()

# 2. Create the embeddings model (this is the best & fastest one in 2025)
embeddings = UpstageEmbeddings(model="solar-embedding-1-large")

# 3. Your texts
texts = [
    "Hello, nice to meet you.",
    "LangChain simplifies the process of building applications with large language models",
    "Retrieval-Augmented Generation (RAG) is an effective technique for improving AI responses.",
]

# 4. Generate embeddings
vectors = embeddings.embed_documents(texts)

# 5. Print results
print(f"Number of texts   : {len(texts)}")
print(f"Embedding dimension: {len(vectors[0])}\n")

for i, (text, vec) in enumerate(zip(texts, vectors)):
    print(f"Text {i+1}: {text}")
    print(f"First 4 values → {vec[:4]}")
    print("-" * 60)