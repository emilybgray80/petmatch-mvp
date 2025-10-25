# backend/main.py
# Minimal FastAPI health endpoint (starter)
from fastapi import FastAPI, File, Form, UploadFile
import uuid, os, json
from ml.embed import generate_embedding

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🐾 PetMatch API is running! Visit /health or /docs"}

UPLOAD_DIR = "backend/uploads"
DATA_DIR = "backend/data"
