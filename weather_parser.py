from datetime import datetime, timedelta
from functions import check_weather, chek_yesterdays_weather
from dotenv import load_dotenv
import os

load_dotenv()  # this loads .env file

api_key = os.getenv("WEATHER_API_KEY")

# api_key = os.getenv("WEATHER_API_KEY")
# if api_key is None:
#     raise ValueError("No API key found! Please set WEATHER_API_KEY.")

# url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

today = datetime.now()
yesterday = today - timedelta(days=1)

print("Today:", today.strftime("%Y-%m-%d"))
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))

with open("cities.txt", "r") as file:
    cities = [line.strip() for line in file if line.strip()]

for city in cities:
    check_weather(today, api_key, city)
    chek_yesterdays_weather(yesterday, api_key, city)
