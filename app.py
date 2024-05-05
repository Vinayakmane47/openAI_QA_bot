from langchain.llms import OpenAI 
from dotenv import load_dotenv 
import streamlit as st 
import os

load_dotenv()


def get_openai_response(question): 
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY") ,temperature=0.6)
    response = llm(question)
    return response 

print(get_openai_response("who is MS dhoni"))

## initiliaze streamlit app 

st.set_page_config(page_title="Q&A demo app")
st.header("Langchain Application")
input = st.text_input("Input:",key="input")
response = get_openai_response(question=input)
submit = st.button("Ask question") 

if submit: 
    st.subheader("The response is ")
    st.write(response)