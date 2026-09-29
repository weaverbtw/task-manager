
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    SECRET_KEY: str = os.environ["SECRET_KEY"]
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()