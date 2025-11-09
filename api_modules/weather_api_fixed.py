import os
import requests

def get_weather(city: str, api_key = "98f5c2d24848471adb878b2bc492036e") -> str:
    if api_key is None:
        api_key = os.getenv("98f5c2d24848471adb878b2bc492036e")
    if not api_key:
        return "OpenWeather API key not provided. Set OPENWEATHER_API_KEY environment variable or pass api_key parameter."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.RequestException as e:
        return f"Failed to fetch weather data: {e}"

    try:
        name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
    except (KeyError, IndexError, TypeError) as e:
        return f"Unexpected response format from API: {e}"

    return f"{name}: {temp}°C, {description}"
