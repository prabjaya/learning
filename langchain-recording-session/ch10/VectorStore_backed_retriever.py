from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document 
from langchain_classic.chains import RetrievalQA
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()




# 1. Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# 2. Initialize Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004"
)

# 3. Create sample documents
documents = [
    Document(page_content="LangChain is a framework for building LLM-powered applications."),
    Document(page_content="Vector stores enable efficient similarity search."),
    Document(page_content="MMR balances relevance and diversity in retrieval."),
    Document(page_content="Google Gemini models are available via langchain-google-genai."),
    Document(page_content="Retrievers fetch relevant documents from vector stores.")
]

# 4. Create VectorStore
vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embeddings
)

# 5. Create VectorStore-backed Retriever with MMR
retriever = vectorstore.as_retriever(
    # search_type="mmr", 
    #  mmr --- > Maximal Marginal Relevance
    search_kwargs={
        "k": 3,
        "fetch_k": 6,
        "lambda_mult": 0.5
    }
)

# 6. Invoke the Retriever directly
query = "What is MMR used for in LangChain?"
retrieved_docs = retriever.invoke(query)

print("Retrieved documents:")
for i, doc in enumerate(retrieved_docs, 1):
    print(f"{i}. {doc.page_content}")

# 7. Use Retriever in a QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff" 
    # stuff --- >All retrieved documents are stuffed into one prompt
)

response = qa_chain.invoke({"query": query})

print("\nLLM Answer:")
print(response["result"])