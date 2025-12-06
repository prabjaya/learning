# Install dependencies if needed:
# pip install langchain langchain-google-genai python-dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 1️⃣ Initialize Google GenAI chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

# 2️⃣ Create prompt
prompt_message = HumanMessage(content="What is the capital of India?")

# 3️⃣ Generate response
response = llm.generate([[prompt_message]])

# 4️⃣ Show the AI response
completion_text = response.generations[0][0].text
print("Response:\n", completion_text)

# 5️⃣ Estimate token usage (roughly)
prompt_tokens_est = len(prompt_message.content.split())
completion_tokens_est = len(completion_text.split())
total_tokens_est = prompt_tokens_est + completion_tokens_est

print("\nEstimated Token Usage:")
print("Prompt Tokens (est):", prompt_tokens_est)
print("Completion Tokens (est):", completion_tokens_est)
print("Total Tokens (est):", total_tokens_est)
