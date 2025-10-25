# backend/main.py
# Minimal FastAPI health endpoint (starter)
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}
