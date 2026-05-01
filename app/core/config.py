import os
from dotenv import load_dotenv

load_dotenv() # Scans parent directories and loads the environment variables from .env file

class Settings:
    PROJECT_NAME: str = 'Car Price Prediction API'
    API_KEY = os.getenv("API_KEY", 'demo-key')
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", 'secret')
    JWT_ALGORITHM = 'HS256'
    MODEL_PATH = 'app/models/model.pkl'
    REDIS_URL = os.getenv("REDIS_URL", 'redis://localhost:6379')

settings = Settings()
