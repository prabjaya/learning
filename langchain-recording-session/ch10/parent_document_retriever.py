from langchain.retrievers.parent_document_retriever import ParentDocumentRetriever
from langchain_chroma import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.storage import InMemoryStore
from langchain.schema import Document
from pydantic import Field


# 1️⃣ Documents
docs = [
    Document(page_content="LangChain is a framework for LLM applications."),
    Document(page_content="FAISS enables fast vector similarity search.")
]

# 2️⃣ Splitters
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=5)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=5)

# 3️⃣ Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4️⃣ Vector Store 
# Chroma handles the index and dimensions automatically.
vectorstore = Chroma(
    collection_name="parents_split",
    embedding_function=embeddings
)

# 5️⃣ In-memory parent document store
docstore = InMemoryStore()

# 6️⃣ ParentDocumentRetriever
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    parent_splitter=parent_splitter,
    child_splitter=child_splitter,
    search_kwargs={"k": 2},
)

# 7️⃣ Add documents
retriever.add_documents(docs)

# 8️⃣ Query
results = retriever.invoke("What is LangChain?")
print(results[0].page_content)