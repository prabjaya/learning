from sentence_transformers import SentenceTransformer

# Load a pre-trained embeddings model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight, fast model

# Example sentences
sentences = [
    "I love coding in Python.",
    "Hugging Face is creating amazing NLP tools."
]

# Generate embeddings
embeddings = model.encode(sentences)

# Print embeddings
for i, emb in enumerate(embeddings):
    print(f"Sentence: {sentences[i]}")
    print(f"Embedding vector (first 5 values): {emb[:5]}\n")  # show first 5 dims for brevity
