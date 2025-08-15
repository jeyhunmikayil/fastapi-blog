# app/core/config.py
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    ALLOWED_ORIGINS: str = "*"  
    BREVO_API_KEY: str
    SENDER_EMAIL: str
    SECRET_KEY: str
    UPLOAD_DIR: str = "uploads"  # default if not in .env
    BASE_URL: str = "http://localhost:8095"

    class Config:
        case_sensitive = True
        env_file = ".env" # load from project root

    @property
    def upload_path(self) -> str:
        """
        Returns absolute path to upload directory & ensures it exists.
        """
        path = os.path.abspath(self.UPLOAD_DIR)
        os.makedirs(path, exist_ok=True)
        return path

settings = Settings()