# 🤖 Jarvis API Fusion

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

**Your Personal AI Assistant powered by Multiple APIs**

*Weather • Cryptocurrency • News • Motivational Quotes • Memory System*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Demo](#-demo) • [API Keys](#-api-keys-setup)

</div>

---

## 📖 Overview

**Jarvis API Fusion** is an intelligent command-line assistant that brings together multiple powerful APIs into one seamless experience. Get real-time weather updates, track cryptocurrency prices, stay informed with the latest news, and get inspired with motivational quotes - all through a simple conversational interface.

### ✨ What Makes It Special?

- 🎯 **Simple Commands** - Natural language interface
- 💾 **Memory System** - Remembers your previous queries
- 🔄 **Error Handling** - Robust fallback mechanisms
- 🌐 **Multiple APIs** - Weather, Crypto, News, and Quotes
- 🚀 **No Dependencies Hell** - Minimal requirements
- 📱 **Cross-Platform** - Works on Windows, Mac, and Linux

---

## 🎯 Features

### 🌦️ Weather Information
Get real-time weather data for any city worldwide
- Current temperature with "feels like" metric
- Weather conditions and descriptions
- Humidity and wind speed
- Powered by **OpenWeather API**

### 💰 Cryptocurrency Prices
Track live cryptocurrency prices
- Support for 10,000+ cryptocurrencies
- Real-time USD pricing
- No API key required!
- Powered by **CoinGecko API**

### 📰 Latest News
Stay updated with top headlines
- Technology, Business, Sports, Health, and more
- Multiple country support (US, UK, India, etc.)
- Customizable categories
- Powered by **NewsAPI**

### 💡 Motivational Quotes
Get inspired with random quotes
- Thousands of quotes from famous personalities
- Automatic fallback to alternative sources
- No API key required!
- Powered by **Quotable & ZenQuotes APIs**

### 💾 Memory System
Never lose track of your queries
- Automatically logs all API calls
- Timestamps for each query
- View history anytime with `memory` command
- Persistent storage in JSON format

---

## 🚀 Installation

### Prerequisites

- **Python 3.7+** installed on your system
- **pip** package manager
- Internet connection

### Step 1: Clone or Download

```bash
# Clone the repository (if using git)
git clone https://github.com/JD-Coder0129/jarvis-api-fusion.git
cd jarvis-api-fusion

# Or simply download and extract the ZIP file
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests
```

### Step 3: Set Up API Keys

See [API Keys Setup](#-api-keys-setup) section below.

---

## 🔑 API Keys Setup

### 🌦️ OpenWeather API (For Weather)

1. **Sign up**: Visit [OpenWeather API](https://openweathermap.org/api)
2. **Get API Key**: Free tier allows 60 calls/minute
3. **Activate**: Wait 10-15 minutes for activation
4. **Set Environment Variable**:

**Windows (CMD):**
```cmd
set OPENWEATHER_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

**Linux/Mac:**
```bash
export OPENWEATHER_API_KEY=your_api_key_here
```

### 📰 NewsAPI (For News)

1. **Sign up**: Visit [NewsAPI](https://newsapi.org/)
2. **Get API Key**: Free tier allows 100 requests/day
3. **Instant Activation**: Works immediately!
4. **Set Environment Variable**:

**Windows (CMD):**
```cmd
set NEWSAPI_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:NEWSAPI_KEY="your_api_key_here"
```

**Linux/Mac:**
```bash
export NEWSAPI_KEY=your_api_key_here
```

> 💡 **Note**: Crypto and Quotes features work without any API keys!

---

## 💻 Usage

### Starting Jarvis

```bash
python ai_api_core_fixed.py
```

You'll see:
```
🤖 Jarvis API Fusion - Online
==================================================
Type 'help' for commands or 'exit' to quit.

You: 
```

### Available Commands

#### 🌦️ Weather Command
```
You: weather Mumbai
🌦️ Mumbai: 28.5°C (feels like 32.1°C)
   Condition: Clear sky
   Humidity: 65%, Wind: 3.5 m/s
```

#### 💰 Crypto Command
```
You: crypto bitcoin
💰 Bitcoin Price: $45,234.56

You: crypto ethereum
💰 Ethereum Price: $2,847.92
```

**Popular Coins**: bitcoin, ethereum, dogecoin, cardano, solana, ripple, polkadot, litecoin

#### 📰 News Command
```
You: news
📰 Top Headlines (US - Technology):
1. OpenAI launches new model - TechCrunch
2. Apple announces new iPhone - The Verge
3. Google updates AI features - BBC Tech

You: news in business
📰 Top Headlines (IN - Business):
1. Stock market hits record high - Economic Times
2. Startup funding surge continues - Business Standard
```

**Countries**: us, in, gb, au, ca, de, fr  
**Categories**: technology, business, sports, health, entertainment, science

#### 💡 Quote Command
```
You: quote
💡 "The only way to do great work is to love what you do." - Steve Jobs
```

#### 💾 Memory Command
```
You: memory
💾 Jarvis Memory Summary:

Weather (3 entries):
  2025-01-15 10:30:45: Mumbai: 28.5°C, clear sky
  2025-01-15 11:15:22: London: 12.3°C, cloudy
  2025-01-15 14:22:10: New York: 5.2°C, snow

Crypto (2 entries):
  2025-01-15 10:31:15: Bitcoin Price: $45,234.56
  2025-01-15 12:45:30: Ethereum Price: $2,847.92
```

#### ❓ Help Command
```
You: help
🧩 Available Commands:
  weather <city>              → Get weather report 🌦️
  crypto <coin>               → Get cryptocurrency price 💰
  quote                       → Get motivational quote 💡
  news [country] [category]   → Get top news 📰
     Examples: news, news us, news in business
     Countries: us, in, gb, au, ca
     Categories: technology, business, sports, health
  memory                      → Show previous results 💾
  exit                        → Shutdown Jarvis 🔴
```

#### 🔴 Exit Command
```
You: exit
👋 Jarvis: Shutting down the API Fusion system...
```

---

## 🎬 Demo

### Quick Demo Session

```bash
$ python ai_api_core.py
🤖 Jarvis API Fusion - Online
==================================================
Type 'help' for commands or 'exit' to quit.

You: weather London
🌦️ London: 12.3°C (feels like 10.1°C)
   Condition: Cloudy
   Humidity: 78%, Wind: 4.2 m/s

You: crypto bitcoin
💰 Bitcoin Price: $45,234.56

You: quote
💡 "Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill

You: news us technology
📰 Top Headlines (US - Technology):
1. AI Revolution continues with new breakthroughs - TechCrunch
2. Apple unveils next-gen products - The Verge
3. Microsoft expands cloud services - Reuters

You: memory
💾 Jarvis Memory Summary:

Weather (1 entries):
  2025-01-15 10:30:45: London: 12.3°C, Cloudy

Crypto (1 entries):
  2025-01-15 10:31:15: Bitcoin Price: $45,234.56

You: exit
👋 Jarvis: Shutting down the API Fusion system...
```

---

## 📁 Project Structure

```
jarvis-api-fusion/
│
├── ai_api_core.py          # Main application file
├── crypto_api.py           # Cryptocurrency API module
├── weather_api.py          # Weather API module
├── news_api.py             # News API module
├── quotes_api.py           # Quotes API module
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── ai_api_memory.json      # Auto-generated memory file
```

---

## 🛠️ Technical Details

### Architecture

```
┌─────────────────────────────────────────┐
│         ai_api_core.py (Main)           │
│  ┌─────────────────────────────────┐   │
│  │   Command Processing Engine      │   │
│  │   - Input parsing                │   │
│  │   - Route to appropriate module  │   │
│  │   - Memory management            │   │
│  └─────────────────────────────────┘   │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┼──────────┬──────────┐
    │          │          │          │
┌───▼───┐  ┌──▼───┐  ┌──▼───┐  ┌───▼────┐
│Weather│  │Crypto│  │ News │  │ Quotes │
│ API   │  │ API  │  │ API  │  │  API   │
└───────┘  └──────┘  └──────┘  └────────┘
```

### Error Handling

- **Network Errors**: Automatic retry with fallback
- **Invalid API Keys**: Clear error messages with help links
- **SSL Issues**: Automatic certificate verification bypass
- **Rate Limits**: Graceful handling with user notification
- **Invalid Input**: Helpful suggestions for corrections

### Memory System

- **Format**: JSON
- **Storage**: Local file (`ai_api_memory.json`)
- **Persistence**: Survives application restarts
- **Structure**: Categorized by API type with timestamps

---

## 🐛 Troubleshooting

### Common Issues

#### ❌ "Module not found" Error
**Solution**: Make sure all files are in the same directory
```bash
# Check files
ls -la  # Linux/Mac
dir     # Windows
```

#### ❌ "API key not provided" Error
**Solution**: Set environment variables before running
```bash
# Check if set
echo %OPENWEATHER_API_KEY%  # Windows CMD
echo $OPENWEATHER_API_KEY   # Linux/Mac
```

#### ❌ "401 Unauthorized" Error
**Solution**: 
1. Check if API key is correct
2. Wait 10-15 minutes for OpenWeather key activation
3. Verify at: https://home.openweathermap.org/api_keys

#### ❌ "No articles found" Error
**Solution**: Try different country code
```
You: news us technology
```

#### ❌ SSL Certificate Error
**Solution**: Already handled! The code automatically bypasses SSL issues.

#### ❌ "City not found" Error
**Solution**: Check spelling or try different format
```
You: weather New York   # ✅ Correct
You: weather newyork    # ❌ Wrong
```

---

## 🎨 Customization

### Change Default Settings

Edit `ai_api_core.py`:

```python
# Change default news country and category
def process_command(self, user_input):
    # ...
    country = parts[1] if len(parts) > 1 else "in"  # Change "in" to your country
    category = parts[2] if len(parts) > 2 else "business"  # Change category
```

### Add More Cryptocurrencies

No changes needed! CoinGecko supports 10,000+ coins. Just use the coin name:
```
You: crypto solana
You: crypto cardano
You: crypto polkadot
```

### Change Memory File Location

Edit `ai_api_core.py`:

```python
def __init__(self):
    self.memory_file = "path/to/your/memory.json"  # Change path
    self.memory = self.load_memory()
```

---

## 📊 API Rate Limits

| API | Free Tier Limit | Notes |
|-----|----------------|-------|
| OpenWeather | 60 calls/minute, 1M calls/month | Plenty for personal use |
| NewsAPI | 100 calls/day | Good for daily updates |
| CoinGecko | 10-50 calls/minute | No API key needed! |
| Quotable | No limit | Free and unlimited |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions

- 🎵 Add music/Spotify API integration
- 📧 Add email functionality
- 🗓️ Add calendar/events API
- 🎮 Add gaming news API
- 🍕 Add food/restaurant API
- 🚗 Add traffic/maps API

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **OpenWeather** - Weather data
- **CoinGecko** - Cryptocurrency prices
- **NewsAPI** - News headlines
- **Quotable & ZenQuotes** - Inspirational quotes
- **Python Requests Library** - HTTP handling

---

## 👨‍💻 Author

Created with ❤️ by **Your Name**

- GitHub: [@JD-Coder0129](https://github.com/JD-Coder0129)
- Instagram: [@jaycoder13(https://www.instagram.com/jaycoder13)]

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

## 📞 Support

Having issues? Here's how to get help:

1. **Check** the [Troubleshooting](#-troubleshooting) section
2. **Search** existing issues on GitHub
3. **Create** a new issue with:
   - Your Python version
   - Operating system
   - Error message (if any)
   - Steps to reproduce

---

<div align="center">

**Made with 🤖 by Jarvis API Fusion**

*Bringing APIs together, one command at a time*

[⬆ Back to Top](#-jarvis-api-fusion)

</div>
