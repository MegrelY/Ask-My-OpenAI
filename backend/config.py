import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-4o" 
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
