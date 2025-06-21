from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routers import include_routers  # Import include_routers if you want to use it
from .settings import settings

app = FastAPI(title="College Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

include_routers(app)  # Use this to include all routers

@app.get("/")
def read_root():
    return {"message": "College Chatbot API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "chatbot.main:app",
        host="0.0.0.0",
        port=settings.SERVICE_PORT,
        reload=settings.DEBUG,
        loop="asyncio"
    )