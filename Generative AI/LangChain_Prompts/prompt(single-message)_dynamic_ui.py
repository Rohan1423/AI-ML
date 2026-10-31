from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')
paper_input = st.selectbox('Select a Research Paper', ['Attention is All You Need', 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding', 'GPT-3: Language Models are Few-Shot Learners','Diffusion Models Beat GANs on Image Synthesis'])

style_input = st.selectbox('Select Explaination Style', ['Beginner-Friendly', 'Technical', 'Code-Oriented', 'Mathematical'])

length_input = st.selectbox('Select Explaination Length', ['Short (1-2 paragraphs)', 'Medium (3-5 paragraphs)', 'Long (detailed explaination)'])

# load the prompt template from the saved JSON file
prompt_template = load_prompt('template.json')

if st.button('Summarize'):
    chain = prompt_template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input})
    st.text(result.content)