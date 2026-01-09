from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="bigscience/bloom-560m",
    provider="hf-inference",
    max_new_tokens=64,
    temperature=0.1,
)

import os
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint

# Use a model hosted for Inference API
repo_id = "bigscience/bloom-560m"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_new_tokens=256,
    temperature=0.1,
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
)

# Prompt template
prompt = PromptTemplate.from_template(
    "Answer the following question concisely:\n{question}"
)

# Create the chain
chain = prompt | llm | StrOutputParser()

response = chain.invoke({"question": "What is the capital of India?"})
print(response)
# Run the chain
question = "What is the capital of India?"
response = chain.invoke({"question": question})

print(f"Question: {question}")
print(f"Answer: {response}")
>>>>>>> 8b4a774 (langchain recording session code added)
