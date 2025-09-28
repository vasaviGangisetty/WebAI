import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")

def search_data(query: str):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }

    response = requests.get(url, params=params)

    try:
        response.raise_for_status()
        results = response.json().get("organic_results", [])
        return [
            {
                "Title": r.get("title", "No title"),
                "Link": r.get("link", "#"),
                "Snippet": r.get("snippet", "")
            }
            for r in results[:5]
        ]
    except Exception as e:
        print("SerpAPI error:", response.text)
        raise Exception("Failed to fetch results from SerpAPI")