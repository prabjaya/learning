import uuid
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.storage import InMemoryByteStore
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1️⃣ Setup Embeddings and Vector Store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(collection_name="full_documents", embedding_function=embeddings)

# 2️⃣ Setup the Byte Store (This fixes your error)
# This store holds the ORIGINAL full documents
store = InMemoryByteStore()

# 3️⃣ Initialize the MultiVectorRetriever
id_key = "doc_id"
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,  # This key links the small chunks to the big parent doc
    search_kwargs={"k": 1},
)

# 4️⃣ Create Documents
docs = [
    Document(page_content="LangChain is a framework for building applications with LLMs. It offers chains, agents, and retrieval tools."),
    Document(page_content="FAISS is a library for efficient similarity search and clustering of dense vectors."),
    Document(page_content="LlamaIndex is a data framework for LLM-based applications to ingest, structure, and access private data.")
]

# 5️⃣ Generate IDs for parent documents
doc_ids = [str(uuid.uuid4()) for _ in docs]

# 6️⃣ Split specific documents into smaller chunks (Child Documents)
# We want to search on these small details, but return the whole document above
child_text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)

sub_docs = []
for i, doc in enumerate(docs):
    _id = doc_ids[i]
    _sub_docs = child_text_splitter.split_documents([doc])
    
    # IMPORTANT: Link child chunk to parent ID
    for _sub_doc in _sub_docs:
        _sub_doc.metadata[id_key] = _id
    sub_docs.extend(_sub_docs)

# 7️⃣ Add data to the Retriever
# Add small chunks to VectorStore (for searching)
retriever.vectorstore.add_documents(sub_docs)
# Add full parents to ByteStore (for returning)
retriever.docstore.mset(list(zip(doc_ids, docs)))

# 8️⃣ Query
# Even though we search for a specific detail ("clustering"), we get the full FAISS doc
query = "clustering" 
results = retriever.invoke(query)

print(f"Query: {query}")
print("-" * 30)
for i, doc in enumerate(results, 1):
    print(f"Result {i} (Full Parent Doc):\n{doc.page_content}\n")