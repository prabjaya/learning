# dataframe_parser.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PandasDataFrameOutputParser  # Correct for LangChain 1.1.0
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import pandas as pd  # Required for DataFrame output

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# 1. Define the expected DataFrame structure (dict format for v1.1.0)
fields = {
    "name": {"type": "string", "description": "Person's full name"},
    "age": {"type": "integer", "description": "Age in years"},
    "city": {"type": "string", "description": "Current city of residence"},
    "job": {"type": "string", "description": "Current job title"},
    "hobby": {"type": "string", "description": "Favorite hobby"}
}

# 2. Create the parser
parser = PandasDataFrameOutputParser(fields=fields)

# 3. Prompt with strict instructions
prompt = PromptTemplate(
    template="""
Extract people mentioned in the text below and return them as a table.

{format_instructions}

Text:
{text}
""",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 4. Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0,
    max_output_tokens=512
)

# 5. Chain
chain = prompt | model | parser

# 6. Run it
text = """
Alice is 30 years old and lives in Paris. She works as a designer and loves painting.
Bob, 25, is a software engineer from Berlin. He enjoys hiking on weekends.
Charlie is 45 and lives in Tokyo. He is a chef and his hobby is photography.
"""

print("Input text:")
print(text)
print("\n" + "="*60)
print("Extracted DataFrame:")
print("="*60)

df = chain.invoke({"text": text})
print(df)