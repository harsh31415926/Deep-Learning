from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

import uvicorn 
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY","")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY', "")
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY', "")


app = FastAPI(
    title = 'Langchain Server',
    version = '1.0',
    description= 'First FastAPI'
)

add_routes(
    app,
    ChatGroq(model="llama-3.1-8b-instant"),
    path="/Chat_Groq"
)

model = ChatGroq(model="llama-3.1-8b-instant")


prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "Write an essay about {topic} around 69 words.")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "Write a poem with rhyming about {topic} around 39 words.")
])

add_routes(
    app, 
    prompt1|model,
    path = "/Essay"
)

add_routes(
    app,
    prompt2|model,
    path = "/Poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
