from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model_name='gpt-6-astra')

# 1st prompt -> detailed report
template1 = PromptTemplate(template='Wriite a detailed report on {topic}',input_variables=['topic'])

# 2nd prompt -> summary in 5 lines
template2 = PromptTemplate(template='Wriite a 5 line summary on the following text. \n {text}',input_variables=['text'])

parser  = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)