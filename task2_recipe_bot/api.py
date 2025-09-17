from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

MODEL_DIR = "t5-small"  # Change to fine-tuned model folder later

tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)
model.eval()

app = FastAPI()

class Query(BaseModel):
    ingredients: str
    max_length: int = 120

@app.post("/generate")
def generate(q: Query):
    input_text = "ingredients: " + q.ingredients
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=q.max_length, num_return_sequences=1)
    recipe = tokenizer.decode(out[0], skip_special_tokens=True)
    return {"ingredients": q.ingredients, "recipe": recipe}
