# backend/main.py
# Minimal FastAPI health endpoint (starter)
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "🐾 PetMatch API is running! Visit /health or /docs"}
@app.get("/health")
def health():
    return {"ok": True}
