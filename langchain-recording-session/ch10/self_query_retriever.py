import os
# New imports (requires pip install langchain-huggingface)
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_chroma import Chroma
from langchain.schema import Document
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever

# 1. Setup Data
docs = [
    Document(page_content="A bunch of scientists bring back dinosaurs", metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"}),
    Document(page_content="Leo DiCaprio gets lost in a dream", metadata={"year": 2010, "rating": 8.2, "genre": "science fiction"}),
    Document(page_content="Three men walk into the Zone", metadata={"year": 1979, "rating": 9.9, "genre": "science fiction"}),
]

# 2. Embeddings (Free & Local)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(docs, embeddings)

# 3. LLM (Free & Cloud)
# You need a specific model that is smart enough to write code/filters. 
# Mistral-7B-Instruct is a good free choice.
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.01,
    huggingfacehub_api_token="YOUR_HUGGINGFACE_TOKEN" # Get from huggingface.co/settings/tokens
)

# 4. Metadata Info
metadata_field_info = [
    AttributeInfo(name="genre", description="The genre of the movie", type="string"),
    AttributeInfo(name="year", description="The year the movie was released", type="integer"),
    AttributeInfo(name="rating", description="A 1-10 rating for the movie", type="float"),
]

# 5. Retriever
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectorstore,
    document_contents="Brief summary of a movie",
    metadata_field_info=metadata_field_info,
    verbose=True
)

# 6. Run
# Try a simple query first to test the LLM's logic
results = retriever.invoke("movies rated above 8.5")

for doc in results:
    print(f"Found: {doc.page_content}")