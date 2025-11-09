import requests

def get_crypto(coin="bitcoin"):
    """
    Fetch cryptocurrency price from CoinGecko API.
    Args:
        coin: Name of the cryptocurrency (default: bitcoin)
    Returns:
        String with price or error message
    """
    try:
        coin_key = coin.lower()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_key}&vs_currencies=usd"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        price = data.get(coin_key, {}).get('usd')
        if price is None:
            return f"Price for '{coin}' not found. Check the coin name."
        return f"{coin.capitalize()} Price: ${price:,.2f}"
    except requests.RequestException as e:
        return f"Network error: {e}"
    except ValueError:
        return "Invalid response received from the API."
    except Exception as e:
        return f"Unexpected error: {e}"
