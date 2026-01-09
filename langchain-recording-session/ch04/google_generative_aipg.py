import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# ChatGoogleGenerativeAI Initialize the language model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# # stream --- >Instead of returning the full response at once, it returns a generator/stream of chunks as the model generates text.
# answer = llm.stream("Explain LangChain in simple terms.")

# # Print the streaming results
# for chunk in answer:
#     print(chunk.content)


# Batch (batch): Multiple prompts → multiple responses at the same time, returned as a list.
results = llm.batch(
    [
        "The capital of Poland?",
        "List 5 major tourist destinations in Poland",
    ]
)
for res in results:
    # Prints the contents of each result.
    print(res.content)