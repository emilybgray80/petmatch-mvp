# backend/main.py
# Minimal FastAPI health endpoint (starter)
# PetMatch MVP backend — includes /, /health, and /api/upload endpoints

from fastapi import FastAPI, File, Form, UploadFile
import uuid, os, json
from ml.embed import generate_embedding

app = FastAPI()

# 🏠 Root route for homepage
@app.get("/")
def home():
    return {"message": "🐾 PetMatch API is running! Visit /health or /docs"}

# 💓 Health check route
@app.get("/health")
def health():
    return {"ok": True}

# 📸 Upload endpoint — saves image + metadata and generates placeholder embedding
UPLOAD_DIR = "backend/uploads"
DATA_DIR = "backend/data"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

@app.post("/api/upload")
async def upload(kind: str = Form(...),
                 date_reported: str = Form(...),
                 lat: float = Form(...),
                 lon: float = Form(...),
                 contact: str = Form(...),
                 file: UploadFile = File(...)):
    id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{id}_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Generate placeholder embedding
    embedding = generate_embedding(file_path)

    record = {
        "id": id,
        "kind": kind,
        "date_reported": date_reported,
        "lat": lat,
        "lon": lon,
        "contact": contact,
        "image": file_path,
        "embedding": embedding
    }

    with open(f"{DATA_DIR}/{id}.json", "w") as f:
        json.dump(record, f, indent=2)

    return {"id": id, "message": "File uploaded successfully with embedding placeholder."}
