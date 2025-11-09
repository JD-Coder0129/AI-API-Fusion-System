import json
from datetime import datetime
from api_modules import get_weather, get_crypto, get_quote, get_news


class AIApiCore:
    def __init__(self):
        self.memory_file = "ai_api_memory.json"
        self.memory = self.load_memory()

    def load_memory(self):
        """Load memory from JSON file."""
        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_memory(self):
        """Save memory to JSON file."""
        try:
            with open(self.memory_file, "w", encoding="utf-8") as file:
                json.dump(self.memory, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving memory: {e}")
            
    def process_command(self, user_input):
        user_input = user_input.lower().strip()

        if user_input.startswith("weather "):
            city = user_input.split(" ", 1)[1]
            result = get_weather(city)
            self.log_result("weather", result)
            print(f"🌦️ {result}")

        elif user_input.startswith("crypto "):
            coin = user_input.split(" ", 1)[1]
            result = get_crypto(coin)
            self.log_result("crypto", result)
            print(f"💰 {result}")

        elif user_input == "quote":
            result = get_quote()
            self.log_result("quote", result)
            print(f"💡 {result}")

        elif user_input.startswith("news"):
            # Parse optional parameters: news [country] [category]
            parts = user_input.split()
            country = parts[1] if len(parts) > 1 else "us"
            category = parts[2] if len(parts) > 2 else "technology"
            
            headlines = get_news(country=country, category=category)
            self.log_result("news", headlines)
            print(f"📰 Top Headlines ({country.upper()} - {category.capitalize()}):")
            for idx, article in enumerate(headlines, 1):
                print(f"{idx}. {article}")

        elif user_input == "memory":
            self.show_memory()

        elif user_input in ["exit", "shutdown", "quit", "bye"]:
            print("\n👋 Jarvis: Shutting down the API Fusion system...")
            self.save_memory()
            return False

        else:
            print("🤔 Jarvis: I don't understand that command yet. Type 'help' for available commands.")

        return True

    def log_result(self, category, data):
        if category not in self.memory:
            self.memory[category] = []
        self.memory[category].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data
        })
        self.save_memory()

    def show_memory(self):
        """Display stored memory of previous API calls."""
        if not self.memory:
            print("🧠 Memory is empty.")
            return
        print("\n💾 Jarvis Memory Summary:")
        for key, entries in self.memory.items():
            print(f"\n{key.capitalize()} ({len(entries)} entries):")
            for entry in entries[-3:]:  # show last 3 results
                timestamp = entry.get('timestamp', 'Unknown time')
                data = entry.get('data', 'No data')
                print(f"  {timestamp}: {data}")

    def run(self):
        """Main loop for the Jarvis system."""
        print("🤖 Jarvis API Fusion - Online")
        print("=" * 50)
        print("Type 'help' for commands or 'exit' to quit.\n")

        running = True
        while running:
            try:
                user_input = input("\nYou: ").strip()
                if not user_input:
                    continue
                if user_input.lower() == "help":
                    self.display_help()
                else:
                    running = self.process_command(user_input)
            except KeyboardInterrupt:
                print("\n\n👋 Jarvis: Interrupted. Shutting down...")
                self.save_memory()
                break
            except Exception as e:
                print(f"Error processing command: {e}")

    def display_help(self):
        """Display available commands."""
        print("\n🧩 Available Commands:")
        print("  weather <city>              → Get weather report 🌦️")
        print("  crypto <coin>               → Get cryptocurrency price 💰")
        print("  quote                       → Get motivational quote 💡")
        print("  news [country] [category]   → Get top news 📰")
        print("     Examples: news, news us, news in business")
        print("     Countries: us, in, gb, au, ca")
        print("     Categories: technology, business, sports, health")
        print("  memory                      → Show previous results 💾")
        print("  exit                        → Shutdown Jarvis 🔴\n")


if __name__ == "__main__":
    jarvis = AIApiCore()
    jarvis.run()