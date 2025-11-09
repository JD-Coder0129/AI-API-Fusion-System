import requests
from requests.exceptions import RequestException
from json import JSONDecodeError
import urllib3

# Disable SSL warnings (only for this module)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_quote():
    url = "https://api.quotable.io/random"
    
    try:
        # Try with SSL verification first
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
    except (RequestException, JSONDecodeError):
        # If SSL fails, try without verification
        try:
            res = requests.get(url, timeout=5, verify=False)
            res.raise_for_status()
            data = res.json()
        except (RequestException, JSONDecodeError) as e:
            # If still fails, try alternative API
            return get_quote_alternative()
    
    try:
        content = data.get('content')
        author = data.get('author')
        if not content or not author:
            return "Error: Missing quote content or author in response"
        return f'"{content}" - {author}'
    except Exception as e:
        return f"Error processing quote: {e}"


def get_quote_alternative():
    url = "https://zenquotes.io/api/random"
    
    try:
        res = requests.get(url, timeout=5, verify=False)
        res.raise_for_status()
        data = res.json()
        
        if isinstance(data, list) and len(data) > 0:
            quote_data = data[0]
            content = quote_data.get('q', '')
            author = quote_data.get('a', 'Unknown')
            if content:
                return f'"{content}" - {author}'
        
        return "Error: Unable to fetch quote at the moment"
        
    except Exception as e:
        return "Error: Quote service temporarily unavailable. Please try again later."