import requests
import streamlit as st

def essay_groq_response(input_text):
    response = requests.post("http://localhost:8000/Essay/invoke", json = {'input':{"topic": input_text }})
    print(response.status_code)
    print(response.text)
    
    return response.json()['output']['content']

def poem_groq_response(input_text):
    response = requests.post("http://localhost:8000/Poem/invoke", json = {'input':{"topic": input_text }})
    
    return response.json()['output']['content']

st.title("Langchain API - Elon Musk's Groq")
input_text1 = st.text_input("Enter your topic for essay here")
input_text2 = st.text_input("Enter your topic for poem here")

if input_text1:
    st.write(essay_groq_response(input_text1))

if input_text2:
    st.write(poem_groq_response(input_text2))