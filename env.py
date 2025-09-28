# env.py
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Access variables safely
SERP_API_KEY = os.getenv("SERP_API_KEY", "your_serpapi_key_here")  # fallback if .env missing
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1")
OLLAMA_PORT = int(os.getenv("OLLAMA_PORT", 11434))