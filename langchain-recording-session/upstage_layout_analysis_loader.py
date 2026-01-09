from dotenv import load_dotenv
from langchain_upstage import UpstageDocumentParseLoader
import os

load_dotenv()

file_path = "storybook.pdf"

loader = UpstageDocumentParseLoader(
    file_path=file_path,
    split="page",
    output_format="text",
)

docs = loader.load()

for i, doc in enumerate(docs[:2]):
    print(f"\n{'='*20} Page {doc.metadata['page']} {'='*20}\n")
    print(doc.page_content)


