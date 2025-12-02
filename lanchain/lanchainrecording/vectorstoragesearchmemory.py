from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS #FAISS(Facebook AI Similarity Search) → Vector database wrapper to store embeddings and perform semantic search.
from langchain_huggingface import HuggingFaceEmbeddings #HuggingFaceEmbeddings → Converts text into vector embeddings using a Hugging Face model.
from langchain_core.documents import Document #Document → Standard schema for text with optional metadata (like source).
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Step 1: Create knowledge base ---
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs = [
    Document(page_content="LangChain helps integrate AI into apps."),
    Document(page_content="LangChain supports chatbots and RAG pipelines."),
    Document(page_content="Google Gemini can be used for text generation and chatbots."),
    Document(page_content="Google Gemini allows generative AI applications."),
]

vectorstore = FAISS.from_documents(docs, embeddings)

# Save to local folder
vectorstore.save_local("faiss_index")
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# --- Step 2: Chat model ---
chat_model = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model="gemini-2.5-flash"
)

# --- Step 3: Manual conversational QA with retrieval ---
def ask_question(question, chat_history):
    # Retrieve relevant documents
    docs = retriever.invoke(question)
    
    # Format context from retrieved documents
    context = "\n".join([doc.page_content for doc in docs])
    
    # Build messages with chat history
    messages = [
        SystemMessage(content=f"You are an assistant for question-answering tasks. Use the following context to answer the question. If you don't know the answer, say that you don't know. Keep the answer concise.\n\nContext:\n{context}")
    ]
    messages.extend(chat_history)
    messages.append(HumanMessage(content=question))
    
    # Get response from chat model
    response = chat_model.invoke(messages)
    return response.content

# --- Step 4: Chat interactions ---
chat_history = []

# First question
question1 = "Tell me something about LangChain."
answer1 = ask_question(question1, chat_history)
print("Answer 1:", answer1)

# Save interaction to history
chat_history.append(HumanMessage(content=question1))
chat_history.append(AIMessage(content=answer1))

# Second question
question2 = "And what about Gemini API?"
answer2 = ask_question(question2, chat_history)
print("Answer 2:", answer2)






