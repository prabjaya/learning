from enum import Enum
from langchain_classic.output_parsers.enum import EnumOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Add it and reload.")

# 1. Define your Enum
class Sentiment(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"

# 2. Create the EnumOutputParser
parser = EnumOutputParser(enum=Sentiment)

# 3. PromptTemplate with VERY strict instructions
prompt = PromptTemplate(
    template=(
        "Classify the sentiment of the following text.\n"
        "You must answer with exactly one word: positive, negative, or neutral.\n"
        "Do not add punctuation, explanations, or formatting.\n\n"
        "Text: {text}\n\n"
        "{format_instructions}"
    ),
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 4. Initialize Google Generative AI LLM (Gemini)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=api_key,  # Explicit (recommended in v1.1.0+)
    temperature=0
)

# 5. Build the chain
chain = prompt | model | parser

# 6. Run it
try:
    result = chain.invoke({"text": "I really dislike waiting in long lines."})
    print("Input: I really dislike waiting in long lines.")
    print(result)        # Sentiment.NEGATIVE
    print(result.value)  # "negative"
    print()
except Exception as e:
    print(f"Error: {e}")

# 7. Run POSITIVE case
try:
    result_positive = chain.invoke({"text": "I absolutely love this product!"})
    print("Input: I absolutely love this product!")
    print("Parsed Enum:", result_positive)         # Sentiment.POSITIVE
    print("Enum value:", result_positive.value) 
    print()
except Exception as e:
    print(f"Error: {e}")

# NEUTRAL case
try:
    result_neutral = chain.invoke({"text": "The sky is blue."})
    print("Input: The sky is blue.")
    print("Parsed Enum:", result_neutral)      
    print("Enum value:", result_neutral.value)  
    print()
except Exception as e:
    print(f"Error: {e}")
