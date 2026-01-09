import os
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from qdrant_client import QdrantClient

# ----------------------------
# CONFIG
# ----------------------------
RESUME_FOLDER = "resumes"
COLLECTION_NAME = "resume_collection"
QDRANT_URL = "http://localhost:6333"

# ----------------------------
# Embeddings
# ----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------
# Load resumes from folder
# ----------------------------
documents = []

for file in os.listdir(RESUME_FOLDER):
    file_path = os.path.join(RESUME_FOLDER, file)

    if file.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()

    elif file.endswith(".txt"):
        loader = TextLoader(file_path)
        docs = loader.load()

    else:
        continue

    # Add filename as metadata
    for doc in docs:
        doc.metadata["file_name"] = file
        doc.metadata["doc_type"] = "resume"

    documents.extend(docs)

print(f"Loaded {len(documents)} document pages")

# ----------------------------
# Split text (important!)
# ----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

split_docs = text_splitter.split_documents(documents)

# ----------------------------
# Store in Qdrant
# ----------------------------
vector_store = Qdrant.from_documents(
    documents=split_docs,
    embedding=embeddings,
    url=QDRANT_URL,
    collection_name=COLLECTION_NAME
)

print("✅ All resumes stored in Qdrant successfully!")
