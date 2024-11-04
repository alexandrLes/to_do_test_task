from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    database_url: str

    # JWT
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 30

    # FastAPI settings
    app_name: str = "To-Do Service API"
    debug: bool = False

    # CORS
    allowed_origins: List[str] = ["http://localhost"]

    class Config:
        env_file = ".env"

# Instantiate the settings
settings = Settings()
