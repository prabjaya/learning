from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# 1. Define documents
docs = [
    Document(page_content="LangChain builds LLM applications"),
    Document(page_content="BM25 is keyword search"),
    Document(page_content="Vector search is semantic"),
    Document(page_content="Hybrid retrieval combines methods"),
]

# 2. BM25 Retriever
bm25 = BM25Retriever.from_documents(docs)
bm25.k = 2

# 3. Vector Retriever
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vs = FAISS.from_documents(docs, embeddings)
vector = vs.as_retriever(search_kwargs={"k": 2})

# 4. Ensemble Retriever
ensemble = EnsembleRetriever(
    retrievers=[bm25, vector],
    weights=[0.5, 0.5],
)

# 5. Query
query = "semantic search"

# 1. BM25 results
bm25_results = bm25._get_relevant_documents(query, run_manager=None)
print("Strict BM25 Retriever Results:")
for r in bm25_results:
    print("-", r.page_content)
    
# 2. Vector results
vector_results = vector.invoke(query)
print("\nVector Retriever Results:")
for r in vector_results:
    print("-", r.page_content)

# 3. Ensemble results
ensemble_results = ensemble.invoke(query)
print("\nEnsemble Retriever Results:")
for r in ensemble_results:
    print("-", r.page_content)
