import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from map import create_map

load_dotenv()
api_key = os.getenv("API_KEY")

@dataclass
class WeatherData:
    city: str
    country: str
    main: str
    description: str
    icon: str
    temperature: int
    feels_like: int
    humidity: int
    windspeed: float
    visibility: float


def get_lat_lon(API_key, city_name, state_code="", country_code=""):
    try:
        resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()   
        data = resp[0]
        lat, lon = data.get("lat"), data.get("lon")
    except Exception:
        lat, lon = 39.9527237, -75.1635262
    
    return lat, lon


def get_current_weather(lat, lon, API_key):
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial").json()
    data = WeatherData(
        city = resp.get("name"),
        country = resp.get("sys").get("country"),
        main = resp.get("weather")[0].get("main"),
        description = resp.get("weather")[0].get("description"),
        icon = resp.get("weather")[0].get("icon"),
        temperature = int(resp.get("main").get("temp")),
        feels_like = int(resp.get("main").get("feels_like")),
        humidity = int(resp.get("main").get("humidity")),
        windspeed = float(resp.get("wind").get("speed")),
        visibility = round((float(resp.get("visibility")))/1609.34, 2)
    )
    
    return data


def get_weather(city_name, state_name="", country_name=""):
    lat, lon = get_lat_lon(api_key, city_name, state_name, country_name)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


def get_map(city_name, state_name="", country_name=""):
    lat, lon = get_lat_lon(api_key, city_name, state_name, country_name)
    create_map(lat, lon)


if __name__ == "__main__":
    print(get_weather())