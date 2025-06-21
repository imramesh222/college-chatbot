
from fastapi import APIRouter
from pydantic import BaseModel
from chatbot.service.chatbot_service import ChatbotService
router = APIRouter(prefix="/chat", tags=["bot"])
chatbot = ChatbotService()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    result = await chatbot.process_message(request)
    return result