import os
import google.generativeai as genai
import requests
from dotenv import load_dotenv

load_dotenv()

def get_contextual_sources(cryptic_message):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    serpapi_key = os.getenv("SERPAPI_API_KEY")

    # Configure Gemini API
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Decode slang or cryptic message
    prompt = f"Decode this slang or cryptic message and explain its meaning clearly:\n\"{cryptic_message}\""
    response = model.generate_content(prompt)
    decoded_message = response.text.strip() if response.text else "No decoded meaning found."

    # Build search query
    search_query = f"Meaning of slang: '{cryptic_message}' as '{decoded_message}'"
    url = "https://serpapi.com/search"
    params = {
        "q": search_query,
        "api_key": serpapi_key,
        "engine": "google",
    }

    try:
        serp_response = requests.get(url, params=params, timeout=10)
        results = serp_response.json()
    except Exception as e:
        return [{
            "title": "SerpAPI Connection Error",
            "link": "",
            "snippet": str(e)
        }]

    print("SERPAPI key:", serpapi_key)
    print("Search query:", search_query)
    print("SerpAPI raw response:", results)

    # Handle missing/empty results gracefully
    if not results or "error" in results or "organic_results" not in results:
        return [{
            "title": "SerpAPI Error",
            "link": "",
            "snippet": results.get("error", "Google hasn't returned any results for this query.")
        }]

    # Extract top 3 results
    links = []
    for result in results.get("organic_results", [])[:3]:
        links.append({
            "title": result.get("title"),
            "link": result.get("link"),
            "snippet": result.get("snippet", "")
        })

    if not links:
        links.append({
            "title": "No sources found",
            "link": "",
            "snippet": "Try a longer or clearer phrase to get better matches."
        })

    return links
