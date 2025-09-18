from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Avatar Chat API"
    name: str = "John Doe"

    openai_api_key: str
    openai_model: str = "gpt-4o-mini"

    history_max: int = 200

    assets_pdf: str = "assets/CV.pdf"
    assets_summary: str = "assets/summary.txt"

    # CORS for dev
    cors_origins: List[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()