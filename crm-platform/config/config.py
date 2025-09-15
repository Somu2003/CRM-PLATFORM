import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database
    DATABASE_URL = "sqlite:///./data/crm_database.db"
    
    # Google OAuth
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "your-google-client-id")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "your-google-client-secret")
    GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8501/auth/callback")
    
    # Gemini AI
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your-gemini-api-key")
    
    # API Settings
    API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key-here")
    
    # Vendor API Simulation
    VENDOR_API_SUCCESS_RATE = 0.9  # 90% success rate
