import requests
import time
from geopy.geocoders import Nominatim

def getLong_Lat(city):
    geocoder = Nominatim(user_agent = 'geo_location.py')
    location = geocoder.geocode(city)  
    return location.longitude, location.latitude

def getWeather(city):
    out = f'The weather in {city} for the upcoming days: '
    LatLong = getLong_Lat(city)
    part = "hourly,current, minutely, lerts"
    api = f'https://api.openweathermap.org/data/2.5/onecall?lat={LatLong[0]}&lon={LatLong[1]}&exclude={part}&units=metric&appid=25b1f9ea27410b714e35abac85e9cdf4'
    json_data = requests.get(api).json()
    for i in range(7):
        date = time.ctime(json_data['daily'][i]["dt"])
        temp = int(json_data["daily"][i]["temp"]["day"])
        condition = json_data["daily"][i]["weather"][0]["main"]
        out += f'\n {date[0:10:]}: {condition}, with temp of: {temp}'
    return out

print(getWeather("oslo"))
print(getWeather("London"))
print(getWeather("Ski"))