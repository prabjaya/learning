from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load saved FAISS index
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# See what documents are inside
print("Stored documents:")
print(vectorstore.docstore._dict) 

# Get vector for a query
query = "Tell me about LangChain"
retrieved_docs = vectorstore.similarity_search(query, k=2)

for doc in retrieved_docs:
    print("Content:", doc.page_content, " | Metadata:", doc.metadata)
