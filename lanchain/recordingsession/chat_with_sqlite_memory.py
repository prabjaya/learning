import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load your Gemini API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# Create SQLite database and table
conn = sqlite3.connect("my_chat.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS chat (
             user_message TEXT,
             gemini_reply TEXT
          )""")
conn.commit()

print("Chat with Gemini! Type 'bye' to stop.\n")

while True:
    # 1. You type something
    message = input("You: ")
    if message.lower() == "bye":
        print("Chat saved! Goodbye!")
        break

    # 2. Send to Gemini and get reply
    reply = llm.invoke(message).content

    # 3. Show reply
    print(f"Gemini: {reply}\n")

    # 4. Save both messages to SQLite
    c.execute("INSERT INTO chat VALUES (?, ?)", (message, reply))
    conn.commit()

# Close database
conn.close()


# Check Your Saved Chat
# Open the database:
# sqlite3 my_chat.db "SELECT * FROM chat;"