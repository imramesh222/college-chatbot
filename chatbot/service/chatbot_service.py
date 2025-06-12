# routers/chatbot_routes.py
from fastapi import APIRouter, HTTPException
from ..domain.chatbot_req_res import ChatRequest, ChatResponse
from ..service.chatbot_service import ChatbotService

router = APIRouter()
service = ChatbotService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        return await service.process_message(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/intents")
async def list_intents():
    return {
        "intents": [
            {"name": "academic_calendar", "description": "Questions about academic calendar dates"},
            {"name": "course_info", "description": "Questions about courses and programs"},
            {"name": "campus_directions", "description": "Questions about locations on campus"},
            {"name": "results_notices", "description": "Questions about exam results and notices"},
            {"name": "faqs", "description": "Frequently asked questions"},
            {"name": "contact", "description": "Contact information queries"}
        ]
    }