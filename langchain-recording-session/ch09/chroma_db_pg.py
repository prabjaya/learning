from dotenv import load_dotenv
import os

from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_chroma import Chroma


# Load environment variables from .env
load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    print("Warning: GEMINI_API_KEY is missing")


# -------------------- Embeddings --------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)


# -------------------- Documents --------------------
docs = [
    Document(page_content="LangChain makes working with LLMs easy.", metadata={"source": "example1"}),
    Document(page_content="Chroma is a vector database.", metadata={"source": "example2"}),
    Document(page_content="Embeddings store semantic meaning of text.", metadata={"source": "example3"}),
]


# -------------------- Chroma Vector DB (Persisted) --------------------
PERSIST_DIR = "./chroma_db"

vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="my_free_collection",
    persist_directory=PERSIST_DIR
)



# -------------------- Gemini LLM --------------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    api_key=gemini_key
)


# -------------------- RetrievalQA Chain --------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=vector_db.as_retriever(search_kwargs={"k": 1})
)


# -------------------- Query --------------------
query = "Which document talks about Chroma?"
answer = qa_chain.invoke({"query": query})

print("\nAnswer:\n", answer)
