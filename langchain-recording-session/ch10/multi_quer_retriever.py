from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.llms import HuggingFacePipeline

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# 1️⃣ Documents
docs = [
    Document(page_content="LangChain is a framework for building applications with LLMs."),
    Document(page_content="FAISS is a library for efficient similarity search and clustering."),
    Document(page_content="Chroma is a vector database optimized for LLM-based retrieval."),
]

# 2️⃣ Split documents into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
splits = splitter.split_documents(docs)

# 3️⃣ Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4️⃣ Vector Store
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    collection_name="multiquery_demo"
)

# 5️⃣ Local HuggingFace model for MultiQueryRetriever
# Using a small, free, CPU-friendly seq2seq model
model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=128
)

llm = HuggingFacePipeline(pipeline=pipe)

# 6️⃣ MultiQueryRetriever
retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    llm=llm,
)

# 7️⃣ Query
query = "What is LangChain used for?"
results = retriever.invoke(query)

# 8️⃣ Print results
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(doc.page_content)
