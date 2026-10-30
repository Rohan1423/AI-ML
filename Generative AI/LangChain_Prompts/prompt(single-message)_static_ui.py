from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')
user_input = st.text_input('Enter your query here')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.text(result.content)