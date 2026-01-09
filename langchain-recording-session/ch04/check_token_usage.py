# Install dependencies if needed:
# pip install langchain langchain-google-genai python-dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#Initialize Google GenAI chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

# Create prompt
prompt_message = HumanMessage(content="What is the capital of India?")

#Generate response
response = llm.generate([[prompt_message]])

#Show the AI response
completion_text = response.generations[0][0].text
print("Response:\n", completion_text)

#Estimate token usage (roughly)
prompt_tokens_est = len(prompt_message.content.split())
completion_tokens_est = len(completion_text.split())
total_tokens_est = prompt_tokens_est + completion_tokens_est

print("\nEstimated Token Usage:")
print("Prompt Tokens:", prompt_tokens_est)
print("Completion Tokens:", completion_tokens_est)
print("Total Tokens:", total_tokens_est)
