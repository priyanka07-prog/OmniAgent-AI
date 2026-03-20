from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression

app = FastAPI()

# -------- Request Model --------
class InputData(BaseModel):
    text: str
    mode: str   # "UI" or "ML"

# -------- Dummy ML Model --------
ml_model = LogisticRegression()

def ml_model_response(text):
    return f"ML Model Response for: {text}"

# -------- Dummy LLM Function --------
def llm_response(text):
    return f"LLM Response for: {text}"

# -------- Main Route --------
@app.post("/process")
def process_input(data: InputData):
    text = data.text
    mode = data.mode

    if mode == "UI":
        result = llm_response(text)
    else:
        result = ml_model_response(text)

    return {
        "input": text,
        "mode": mode,
        "response": result
    }