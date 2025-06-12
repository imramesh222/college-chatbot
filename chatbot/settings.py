# settings.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "College Chatbot API"
    allowed_origins: list = ["http://localhost:3000", "https://yourcollege.edu"]
    database_url: str = "sqlite:///./college_chatbot.db"

    class Config:
        env_file = ".env"


settings = Settings()