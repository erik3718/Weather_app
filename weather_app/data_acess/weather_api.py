import requests
import json
from datetime import datetime, timezone
from geopy.geocoders import Nominatim


def geo_quest(name):
    global temp_in_c, sky_clearance, zone_of_time, pressure, humidity, sky_clearance, wind_speed, feels_like, sunrise_time, sunset_time, wind_speed_km, temp_in_c_feels, temp_in_c, latitude, longitude
    loc = Nominatim(user_agent="GetLoc")
    name = name.strip().replace("'", "").replace('"', "")
    getLoc = loc.geocode(name)
    latitude = int(getLoc.latitude)
    longitude = int(getLoc.longitude)
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": longitude,
        "lon": latitude,
        "exclude": "hourly,daily",
        "appid": "0a599438025fef20aceb13b8ee6b4223" # Your API key
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()
    current = data.get("current", {})
    zone_of_time = data.get("timezone", "N/A")
    temperature = int(current.get("temp", "N/A"))
    description = current.get("weather", "N/A") # skip
    pressure = current.get("pressure", "N/A") #izrazi ga sa hPa
    humidity = current.get("humidity", "N/A") #izrazi ga sa %
    sky_clearance = description[0]["description"]
    sunrise = current.get("sunrise", "N/A")
    sunset = current.get("sunset", "N/A")
    wind_speed = current.get("wind_speed", "N/A")
    feels_like = current.get("feels_like", "N/A")
    sunrise_time = datetime.fromtimestamp(sunrise, timezone.utc).strftime("%H:%M:%S")
    sunset_time = datetime.fromtimestamp(sunset, timezone.utc).strftime("%H:%M:%S")
    wind_speed_km =int(wind_speed * 3.6)
    temp_in_c_feels = int(feels_like - 273.15)
    temp_in_c = int(temperature - 273.15)
    print(temp_in_c)

geo_quest('Jeruzalem')