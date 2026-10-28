from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about Bumrah'

query_embedding = embeddings.embed_query(query)
document_embeddings = embeddings.embed_documents(documents)

# Always pass 2D arrays to cosine_similarity, even if you have only one query or document. The function expects 2D arrays for both inputs.
scores = cosine_similarity([query_embedding], document_embeddings)[0]

# to remember the index of the document with the highest similarity score, we can use the following line:
# [-1] -> This will give us the last element of the sorted list, which corresponds to the document with the highest similarity score.
index, score = (sorted(list(enumerate(scores)),key=lambda x: x[1])[-1])
print(documents[index])
print("Similarity Score:",score)