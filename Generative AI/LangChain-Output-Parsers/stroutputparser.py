from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model_name='gpt-6-astra')

# 1st prompt -> detailed report
template1 = PromptTemplate(template='Wriite a detailed report on {topic}',input_variables=['topic'])

# 2nd prompt -> summary in 5 lines
template2 = PromptTemplate(template='Wriite a 5 line summary on the following text. \n {text}',input_variables=['text'])

prompt1 = template1.invoke({'topic':'black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)

print(result2.content)