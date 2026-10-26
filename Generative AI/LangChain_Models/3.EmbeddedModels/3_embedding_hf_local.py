from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Bangalore is the IT hub of India",
    "Chennai is the cultural capital of India"
]

vector = embedding.embed_documents(documents)

print(str(vector))