from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

from dotenv import load_dotenv
import os
load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")

# === 1. Setup Gemini ===
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

# === 2. Create memory (this remembers everything) ===
memory = ChatMessageHistory()

# === 3. Build LCEL Chain with memory ===
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Be friendly!"),
    MessagesPlaceholder(variable_name="history"),   # This adds past chat
    ("human", "{input}")                           # User's new message
])

chain = prompt | llm

# === 4. Simple chat loop ===
print("LCEL Chain with Memory! (type 'quit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Goodbye!")
        break

    # Add user message to memory
    memory.add_user_message(user_input)

    # Run chain (includes full history automatically)
    response = chain.invoke({
        "input": user_input,
        "history": memory.messages
    })

    # Show AI reply
    print(f"Gemini: {response.content}\n")

    # Save AI reply to memory
    memory.add_ai_message(response.content)