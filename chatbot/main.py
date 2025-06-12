# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.chatbot_routes import router as chatbot_router
from .settings import settings

app = FastAPI(title="College Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "College Chatbot API is running"}