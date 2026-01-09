import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumps, loads

# Step 0: Load environment variables
load_dotenv() 

# Step 1: Create a prompt template
prompt = PromptTemplate.from_template("What is the color of {fruit}?")

# Step 2: Initialize the LLM (Google Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

# Step 3: Create a chain
chain = prompt | llm

# Step 4: Serialize (save) the chain to disk using LangChain's serialization
serialized = dumps(chain)
with open("fruit_chain.json", "w") as f:
    f.write(serialized)

print("Chain has been saved to 'fruit_chain.json'.")

# Step 5: Load (deserialize) the prompt from disk and recreate chain
with open("fruit_chain.json", "r") as f:
    serialized_data = f.read()

print("Chain configuration has been loaded from 'fruit_chain.json'.")

# Recreate the LLM with API key (can't serialize secrets)
llm_reloaded = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

# Recreate the chain with the reloaded LLM
loaded_chain = prompt | llm_reloaded

# Step 6: Call the loaded chain
fruits = ["apple", "banana", "grape"]

for fruit in fruits:
    response = loaded_chain.invoke({"fruit": fruit})
    print(f"Fruit: {fruit} --> Color: {response.content}")