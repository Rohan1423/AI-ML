from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temperature: Controls the randomness of the output. Higher values (e.g., 1.0) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic.
# max_completion_tokens: Specifies the maximum number of tokens (words or word pieces) that the model can generate in its response. Setting this limit helps control the length of the output and can prevent excessively long responses.
model = ChatOpenAI(model='gpt-4',temperature=1.5,max_completion_tokens=10)
result = model.invoke("Write a 5 line poem on cricket")
print(result.content)