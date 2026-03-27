# $env:PATH += ";C:\Users\harsh\AppData\Local\Programs\Ollama"
# Run this everytime you open a new terminal


from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY","")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY', "")
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY', "")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that talks in a very professional way and use very hard vocabulary"),
        ("user" , "Question: {question}"),
    ]
)

st.title("Langchain Using Elon Musk's Groq")
input_text = st.text_input("Enter your question here")

# #Calling OLLama

# llm = ChatOpenAI(model="gpt-3.5-turbo")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))

    