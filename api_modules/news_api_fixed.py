import os
import requests
from requests.exceptions import RequestException

def get_news(api_key="b10c961d5f5b4803b18d200305656308", country="us", category="technology", limit=5):
    if api_key is None:
        api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        return ["⚠️ News API key is required. Get free key from: https://newsapi.org"]

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": category, 
        "country": country, 
        "apiKey": api_key, 
        "pageSize": limit
    }
    
    try:
        res = requests.get(url, params=params, timeout=10)
        
        # Check for specific error codes
        if res.status_code == 401:
            return ["❌ Invalid API key. Please check your NEWSAPI_KEY."]
        elif res.status_code == 426:
            return ["❌ API key issue. Please verify your NewsAPI account."]
        elif res.status_code == 429:
            return ["❌ Rate limit exceeded. Try again later."]
        
        res.raise_for_status()
        data = res.json()
        
    except RequestException as e:
        return [f"❌ Network error when fetching news: {e}"]
    except ValueError as e:
        return ["❌ Invalid JSON response from news API"]

    # Check API response status
    if data.get("status") != "ok":
        error_msg = data.get("message", "Unknown error")
        return [f"❌ API Error: {error_msg}"]

    articles = data.get("articles") or []
    
    if not articles:
        # Try without category as fallback
        print("⚠️ No articles found with category filter. Trying general news...")
        params_backup = {
            "country": country,
            "apiKey": api_key,
            "pageSize": limit
        }
        try:
            res = requests.get(url, params=params_backup, timeout=10)
            res.raise_for_status()
            data = res.json()
            articles = data.get("articles") or []
        except:
            pass
    
    if not articles:
        return [
            f"❌ No news articles found for country '{country}' and category '{category}'.",
            "💡 Tip: Try different country codes like 'us', 'gb', 'in', 'au'"
        ]
    
    result = []
    for a in articles[:limit]:
        title = a.get("title") or "No title"
        source = (a.get("source") or {}).get("name") or "Unknown source"
        description = a.get("description") or ""
        
        # Clean up title (remove source suffix if present)
        if " - " in title:
            title = title.split(" - ")[0]
        
        result.append(f"{title} - {source}")
    
    return result