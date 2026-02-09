from fastapi import FastAPI

app = FastAPI(title="Fullstack Growth Journey API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "API is running. Go to /docs or /health"}