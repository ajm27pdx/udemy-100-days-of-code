import requests
from auth import OWM_id

parameters = {
    'lat': 45.5202471,
    'lon': -122.674194,
    'appid': OWM_id,
    'exclude': 'current,minutely,daily'
}
#https://api.openweathermap.org/data/2.8/onecall?lat=45.5202471&lon=-122.674194&appid=b46251243caf85f31844ccabb8be9891
response = requests.get('https://api.openweathermap.org/data/2.8/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
