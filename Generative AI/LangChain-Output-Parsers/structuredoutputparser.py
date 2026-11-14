from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI(model_name='gpt-6-astra')

# Schema Enforce -> Define before parser
schema = [
    ResponseSchema(name='fact1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact3',description='Fact 3 about the topic')
]

parser = parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(template='Give 3 facts about the {topic} \n {format_instruction}',input_variables=['topic'],partial_variables={'format_instruction':parser.get_format_instructions()})

# These following three steps we can also do using chain = template | model | parser, result = chain.invoke({}) -> when no input_variable then send blank dict
prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)