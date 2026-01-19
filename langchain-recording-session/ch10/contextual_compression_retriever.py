from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_classic.chains import RetrievalQA
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors.embeddings_filter import EmbeddingsFilter

import os
from dotenv import load_dotenv
load_dotenv()

# 1️⃣ Initialize LLM and Embeddings
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_retries=6,
    request_timeout=60 
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004"
)
 
# 2️⃣ Create sample documents
documents = [
    Document(page_content="LangChain is a framework for building LLM-powered applications."),
    Document(page_content="Vector stores enable efficient similarity search."),
    Document(page_content="In LangChain, MMR is used to balance relevance and diversity in retrieval."),
    Document(page_content="Google Gemini models are available via langchain-google-genai."),
    Document(page_content="Retrievers fetch relevant documents from vector stores.")
]

# 3️⃣ Create VectorStore and Base Retriever
vectorstore = FAISS.from_documents(documents, embedding=embeddings)

# We retrieve more docs initially (k=4) because the filter will cut some out
base_retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4} 
)

# 4️⃣ Create EmbeddingsFilter
# This compares the query embedding to document embeddings.
# Docs with similarity < 0.6 will be dropped.
embeddings_filter = EmbeddingsFilter(
    embeddings=embeddings, 
    similarity_threshold=0.6
)

# 5️⃣ Create Contextual Compression Retriever
# We pass the filter directly as the 'base_compressor'
contextual_retriever = ContextualCompressionRetriever(
    base_compressor=embeddings_filter,
    base_retriever=base_retriever
)

# 6️⃣ Query the Retriever
query = "What is MMR used for in LangChain?"
retrieved_docs = contextual_retriever.invoke(query)

print(f"Retrieved Documents (Filtered by Embedding Similarity > 0.6):")
if not retrieved_docs:
    print("No documents met the similarity threshold.")
else:
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"{i}. {doc.page_content}")

# 7️⃣ Use Retriever in RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=contextual_retriever,
    chain_type="stuff"
)

# This will now only make 1 LLM call (for the final answer)
response = qa_chain.invoke({"query": query})

print("\nLLM Answer:")
print(response["result"])