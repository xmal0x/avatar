from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pydantic import BaseModel

app = FastAPI(title="Starter API")

# CORS для dev (Vite на 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Starter API is running"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!!!"}

@app.get("/api/time")
def time():
    return {"now": datetime.utcnow().isoformat() + "Z"}

@app.post("/api/message")
def message(payload: Message):
    return {"result": payload.message + "!!!!"}