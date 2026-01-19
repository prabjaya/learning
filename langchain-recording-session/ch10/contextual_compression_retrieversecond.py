# -------------------------------
# langchain_v1.2.2 ContextualCompressionRetriever + Filters Example
# -------------------------------

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_classic.chains import RetrievalQA
from langchain_classic.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate  


# Contextual compression & filters
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors.chain_extract import LLMChainExtractor
from langchain_classic.retrievers.document_compressors.chain_filter import LLMChainFilter
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
base_retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}  # top 3 docs 
)

# 4️⃣ Create Contextual Compressor
compressor = LLMChainExtractor.from_llm(llm)

# 5️⃣ Create Filters


# 5a. LLMChainFilter - keeps documents judged relevant by LLM
prompt = PromptTemplate(
    input_variables=["document", "query"],
    template=(
        "Given the query: '{query}', does the following document help answer it?\n"
        "Document: '{document}'\n"
        "Answer YES or NO."
    )
)
llm_chain = LLMChain(llm=llm, prompt=prompt)
llm_filter = LLMChainFilter(llm_chain=llm_chain)

# 5b. EmbeddingsFilter - keep docs with similarity > threshold
emb_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.6)

    
# Remove the LLMChainFilter from the list to save calls
contextual_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever,
    post_retriever_filter=[emb_filter] 
)

# 7️⃣ Query the Retriever
query = "What is MMR used for in LangChain?"
retrieved_docs = contextual_retriever.invoke(query)

print("Retrieved Documents (compressed & filtered):")
for i, doc in enumerate(retrieved_docs, 1):
    print(f"{i}. {doc.page_content}")

# 8️⃣ Use Retriever in RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=contextual_retriever,
    chain_type="stuff"  # stuff all retrieved docs into the prompt
)

response = qa_chain.invoke({"query": query})
print("\nLLM Answer:")
print(response["result"])
