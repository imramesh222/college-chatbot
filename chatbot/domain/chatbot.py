# domain/chatbot.py
from enum import Enum
from pydantic import BaseModel
from typing import Optional

class IntentType(str, Enum):
    ACADEMIC_CALENDAR = "academic_calendar"
    COURSE_INFO = "course_info"
    CAMPUS_DIRECTIONS = "campus_directions"
    RESULTS_NOTICES = "results_notices"
    FAQS = "faqs"
    CONTACT = "contact"

class ChatbotRecord(BaseModel):
    intent: IntentType
    question: str
    answer: str
    entities: Optional[dict] = None