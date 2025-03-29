# config.py 
import os
import dotenv as env
from pydantic_settings import BaseSettings


env.load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')

    # Jwt
    ALGORITHM: str = 'HS256'
    TOKEN_SECRET: str = os.getenv('TOKEN_SECRET')
    EXPIRATION_SECONDS: int = 60 * 60 * 5  # 5 Hours

settings = Settings()