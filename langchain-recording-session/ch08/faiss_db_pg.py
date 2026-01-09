# pip install langchain langchain-huggingface sentence-transformers langchain-community faiss-cpu langchain-google-genai python-dotenv transformers torch

from dotenv import load_dotenv
import os

from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import FAISS


# -------------------- Load environment variables --------------------
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")


# -------------------- Embeddings --------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# -------------------- Prepare Documents --------------------
docs = [
    Document(page_content="LangChain makes working with LLMs easy.", metadata={"source": "example1"}),
    Document(page_content="FAISS is a vector database used for similarity search.", metadata={"source": "example2"}),
    Document(page_content="Embeddings store semantic meaning of text.", metadata={"source": "example3"}),
]

# -------------------- Create FAISS Vector DB --------------------
vector_db = FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)

print("FAISS vector store created successfully")

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
query = "Which document mentions Embeddings?"
answer = qa_chain.invoke({"query": query})

print("\nAnswer:\n", answer)
