import time
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Enable SQLite cache (stored in llm_cache.sqlite)
set_llm_cache(SQLiteCache(database_path="llm_cache.sqlite"))

# Create model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

messages = [HumanMessage(content="Tell me about Python.")]

# Simple print first 200 characters
def print_short(resp):
    print(resp.content[:200])

# First call
start = time.time()
response1 = llm.invoke(messages)
print("First call:", round(time.time() - start, 3), "seconds")
print_short(response1)

# Second call (cached)
start = time.time()
response2 = llm.invoke(messages)
print("Second call (cached):", round(time.time() - start, 3), "seconds")
print_short(response2)
