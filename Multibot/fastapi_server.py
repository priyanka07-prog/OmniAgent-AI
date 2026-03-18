from fastapi import FastAPI
from app.main import run_agent

app = FastAPI()

@app.get("/chat")
def chat(query: str):
    return {"response": f"You said: {query}"}

@app.get("/agent")
def run_agent_endpoint():
    return {"response": "response"}