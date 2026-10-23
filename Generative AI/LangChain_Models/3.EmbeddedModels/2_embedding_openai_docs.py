from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# dimensions=32 is the default for text-embedding-3-large, but you can specify it explicitly if you want to be clear about the embedding size.
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Bangalore is the IT hub of India",
    "Chennai is the cultural capital of India"
]

result = embedding.embed_documents(documents)

print(str(result))