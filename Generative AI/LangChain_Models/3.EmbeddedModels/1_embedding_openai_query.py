from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# dimensions=32 is the default for text-embedding-3-large, but you can specify it explicitly if you want to be clear about the embedding size.
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))