# PetMatch MVP

AI-powered lost & found pet matching system for Los Angeles (±50 miles).

## Structure
- backend/ : FastAPI backend for uploads and data storage
- ml/ : placeholder for AI embedding code
- backend/uploads/ : uploaded images
- backend/data/ : stored metadata

## Run (for developers)
1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
2. Run FastAPI server:
   ```bash
   uvicorn backend.main:app --reload
   ```
3. Visit [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
