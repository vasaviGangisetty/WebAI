import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def search_web(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://duckduckgo.com/html/?q={urllib.parse.quote(query)}"

    # Step 1: Search DuckDuckGo
    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # Step 2: Get top result URL
    links = soup.select('.result__a')
    if not links:
        return {"error": "No results found"}

    raw_link = links[0]['href']
    match = re.search(r'uddg=([^&]+)', raw_link)
    if match:
        top_url = urllib.parse.unquote(match.group(1))
    else:
        top_url = raw_link
        if top_url.startswith('//'):
            top_url = 'https:' + top_url

    # Step 3: Fetch the page HTML
    try:
        page = requests.get(top_url, headers=headers)
        return {"html": page.text, "url": top_url}
    except Exception as e:
        return {"error": f"Failed to fetch content: {str(e)}"}

def summarize_html(html_content, max_sentences=5):
    """Extracts plain text and returns a short summary."""
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=" ", strip=True)

    # Naive split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    summary = " ".join(sentences[:max_sentences])

    return summary if summary else "Could not generate summary."
