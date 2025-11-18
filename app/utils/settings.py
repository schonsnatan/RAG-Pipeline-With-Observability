import os
from platform import system
from dotenv import load_dotenv, find_dotenv

class Settings:
    load_dotenv()

    ENV_FILE = find_dotenv()
    SYSTEM = system()

    GROQ_API = os.getenv("GROQ_API_KEY")
    QDRANT_HOST = "localhost"
    QDRANT_PORT = "6333"

settings = Settings()