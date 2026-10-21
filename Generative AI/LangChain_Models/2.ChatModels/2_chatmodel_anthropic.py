from langchain import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-v1',temperature=1.5,max_completion_tokens=10)
result = model.invoke("Write a 5 line poem on cricket")
print(result.content)