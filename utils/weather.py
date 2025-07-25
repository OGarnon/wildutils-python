"""
weather.py
Simulates random weather information for a given city.
"""
import random  # Randomly select weather conditions

def show_weather(city):
    # Possible mock weather conditions and emojis
    mock_weather = {
        "Sunny": "\U0001F31E",
        "Rain": "\U0001F327",
        "Cloudy": "\u2601\ufe0f"
    }
    condition = random.choice(list(mock_weather.keys()))  # Random condition
    temp = random.randint(15, 30)  # Random temperature
    print(f"Weather in {city}: {condition} {mock_weather[condition]}, {temp}°C (Mocked)")
