from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.orchestrator import orchestrate

app = FastAPI()

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

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "HIVE OS Backend Running"
    }


@app.post("/chat")
def chat(req: ChatRequest):

    result = orchestrate(req.message)

    return { 
        "reply": result["final"],
        "research": result["research"],
        "engineer": result["engineer"],
        "designer": result["designer"],
        "documentation": result["documentation"],
        "qa": result["qa"],

        "generated_files": result["generated_files"],
        "execution_logs": result["execution_logs"],
    }