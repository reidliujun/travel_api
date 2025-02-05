from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/travel_db"
    AI_API_KEY: str = "your-ai-api-key"
    CACHE_EXPIRY_DAYS: int = 7
    AI_MODEL: str = "ai model"
    AI_ENDPOINT: str = "ai endpoint"

    class Config:
        env_file = ".env"

settings = Settings()