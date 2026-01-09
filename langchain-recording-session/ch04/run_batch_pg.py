from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ChatGoogleGenerativeAI Initialize the language model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

results = llm.batch(
    [
        "The capital of Poland?",
        "List 5 major tourist destinations in Poland",
    ]
)

for res in results:
    # Prints the contents of each result.
    print(res.content)