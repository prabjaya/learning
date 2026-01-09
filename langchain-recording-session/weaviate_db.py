# weaviate : steps
# docker run -d \
#   -p 8080:8080 \
#   -p 50051:50051 \
#   --name weaviate \
#   cr.weaviate.io/semitechnologies/weaviate:1.28.0


#   http://localhost:8080/
#   http://localhost:8080/v1/schema
#   http://localhost:8080/v1/objects

import weaviate
from langchain_weaviate import WeaviateVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# 1. CONFIGURATION
WEAVIATE_URL = "http://localhost:8080"  
COLLECTION_NAME = "Employee_Docs"       


client = weaviate.connect_to_local()
# Clean up old data before starting
if client.collections.exists(COLLECTION_NAME):
    client.collections.delete(COLLECTION_NAME)
    print(f"Deleted existing collection: {COLLECTION_NAME}")


# 2. INITIALIZE EMBEDDING MODEL
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 3. CONNECT TO WEAVIATE (v4 Client)
# connects to localhost:8080 by default
client = weaviate.connect_to_local()

try:
    # 4. PREPARE DOCUMENTS
    docs = [
        Document(page_content="The marketing team meets every Friday at 10 AM."),
        Document(page_content="The engineering team uses Python and Go for backend services."),
        Document(page_content="HR policies regarding remote work were updated in 2024."),
    ]

    
    # 5. CREATE INDEX & STORE EMBEDDINGS
    # .from_documents() automatically creates the Collection (Index) 
    # and generates/stores vectors for the documents.
    vector_store = WeaviateVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        client=client,
        index_name=COLLECTION_NAME,
    )
    print(f"✅ Documents stored in Weaviate collection: '{COLLECTION_NAME}'")
    
    # 6. PERFORM SIMILARITY SEARCH
    query = "What languages do the developers use?"
    
    # Search for top 1 similar documents
    results = vector_store.similarity_search(query, k=1)

    print("\nSearch Results:")
    for i, doc in enumerate(results, start=1):
        print(f"{i}. {doc.page_content}")

finally:
    # Always close the client connection
    client.close()