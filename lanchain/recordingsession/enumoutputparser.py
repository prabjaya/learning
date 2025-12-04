from enum import Enum
from langchain_classic.output_parsers.enum import EnumOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY  is not found in .env file")

# define the Enum
class Sentiment(Enum):
    POSITIVE ="postitive"
    NEGATIVE ="negative"
    NEUTRAL = "neutral"

# create the EnumOutputParser
parser = EnumOutputParser(enum=Sentiment)

# Define the prompt
prompt = PromptTemplate(
    template= ("classify  the sentiment of the following text.\n"
               "you must the answer with exactly one word: positive, nagative, neutral.\n"
               "Do not add any punctioation, explanation or formating.\n"
               "Text:{text}\n\n"
               "{format_instruction}"),
               input_variables=["text"],
               partial_variables={"format_instruction" : parser.get_format_instructions()},

)
# Define the Model
model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = api_key,
    temperature=0
)

# Build the chain
chain = prompt | model | parser

# Run it
result = chain.invoke({"text": "I Realy dislike waiting in long lines"})
print("parsed Enum",result)
print("Enum value:", result.value)

resultsecond = chain.invoke({"text": "The sky is blue"})
print("parsed Enum",resultsecond)
print("Enum value:", resultsecond.value)


