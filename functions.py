import requests
import os
import json

def check_weather(date, api, city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api}&q={city}&days=7&aqi=no&alerts=no"
    response = requests.get(url).json()

    year = date.strftime("%Y")   # '2025'   
    month = date.strftime("%m")  # '04'
    day = date.strftime("%d")    # '28'

    folder_path = os.path.join(year, month, day)
    os.makedirs(folder_path, exist_ok=True)

    # Build file path
    file_path = os.path.join(folder_path, city + ".json")

    # Write API output
    with open(file_path, "w") as file:
        json.dump(response, file, indent=4)



# https://api.weatherapi.com/v1/history.json?key=YOUR_API_KEY&q=Almaty&dt=2025-04-27

def chek_yesterdays_weather(date, api, city):
    url = f"https://api.weatherapi.com/v1/history.json?key={api}&q={city}&dt={date}"
    response = requests.get(url).json()

    year = date.strftime("%Y")   # '2025'   
    month = date.strftime("%m")  # '04'
    day = date.strftime("%d")    # '28'

    folder_path = os.path.join("history", year, month, day)
    os.makedirs(folder_path, exist_ok=True)

    # Build file path
    file_path = os.path.join(folder_path, city + ".json")

    # Write API output
    with open(file_path, "w") as file:
        json.dump(response, file, indent=4)
