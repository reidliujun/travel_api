from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/travel_db"
    DEEPSEEK_API_KEY: str = "your-deepseek-api-key"
    CACHE_EXPIRY_DAYS: int = 7

    class Config:
        env_file = ".env"

settings = Settings()