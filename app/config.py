# Placeholder for application configuration

from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):

    # ==========================
    # Database Configuration
    # ==========================
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "root 123"
    DB_NAME: str = "school_management_db"

   
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()


class Settings:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./school.db")
    app_name: str = os.getenv("APP_NAME", "School Management")
    debug: bool = os.getenv("DEBUG", "false").lower() in ("1", "true", "yes")


settings = Settings()
