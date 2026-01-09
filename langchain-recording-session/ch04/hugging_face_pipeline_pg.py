import warnings
warnings.filterwarnings('ignore')

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts.prompt import PromptTemplate

# ✅ Instruction-tuned pipeline
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=50   
     )     

# ✅ Wrap with updated HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=generator)

# ✅ Prompt template
prompt = PromptTemplate.from_template(
    "Write a detailed paragraph of at least 5 sentences{topic}:"
)

chain = prompt | llm

# Topics
topics = ["google"]

# Generate outputs
for topic in topics:
    result = chain.invoke({"topic": topic})
    print(f"Topic: {topic} --> {result}\n")