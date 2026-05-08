from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_method=["*"],
    allow_headers=["*"],
)

# 라우터
app.include_router(ai.router)

@app.get("/")
def health_check():
    return {
        "status": "AI Server Running"
    }