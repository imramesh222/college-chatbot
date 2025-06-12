# model/chatbot_record.py
from sqlalchemy import Column, String, JSON
from ..utils.common import Base


class ChatbotRecord(Base):
    __tablename__ = "chatbot_records"

    id = Column(String, primary_key=True, index=True)
    intent = Column(String, index=True)
    question = Column(String)
    answer = Column(String)
    entities = Column(JSON)