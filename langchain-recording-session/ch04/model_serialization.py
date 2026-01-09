import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables (ensure GEMINI_API_KEY is in your .env)
load_dotenv()

# Step 1: Create a prompt template
prompt = PromptTemplate.from_template("{fruit} What is the color of?")
# Step 2: Check if the class is serializable
print(f"ChatGoogleGenerativeAI class serializable? {ChatGoogleGenerativeAI.is_lc_serializable()}")

# Step 3: Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)
# Step 4: Check if this instance is serializable
print(f"ChatGoogleGenerativeAI instance serializable? {llm.is_lc_serializable()}")

# Step 5: Create a chain
chain = prompt | llm
# Step 6: Check if the chain is serializable
print(f"Chain serializable? {chain.is_lc_serializable()}")
