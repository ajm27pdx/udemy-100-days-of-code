import requests
from datetime import datetime
import pytz
MY_LAT = 45.512230
MY_LNG = -122.658722

## Get ISS Location Data
response = requests.get(url='http://api.open-notify.org/iss-now.json')
data = response.json()  # jsonify the response
print(response.status_code)  # get status code from response
response.raise_for_status()  # raise exception if error response

iss_lat = float(data['iss_position']['latitude'])
iss_lng = float(data['iss_position']['longitude'])
iss_loc = (iss_lat, iss_lng)

## Get Sunrise and Sunset Data with Localization
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
local_timezone = pytz.timezone("America/Los_Angeles")
data = response.json()
sr = data['results']['sunrise']
ss = data['results']['sunset']
sunrise = datetime.strptime(sr, '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=pytz.utc).astimezone(local_timezone)
sunset = datetime.strptime(ss, '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=pytz.utc).astimezone(local_timezone)
now_time = datetime.now()

# print(data)
# print(datetime.utcnow())
print(f'sunrise is at {sunrise.hour}, sunset is at {sunset.hour}')
print(f'it is now {now_time.hour}')
nighttime = False
if sunrise.hour <= now_time.hour <= sunset.hour:
    print('it is daytime')
else:
    nighttime = True
print(f'the ISS is currently over {iss_loc}')
iss_overhead = False
if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LNG - 5 < iss_lng < MY_LNG + 5:
    print('The ISS is overhead-ish')
    iss_overhead = True
else:
    print('The ISS is not overhead')

if nighttime and iss_overhead:
    print(f'You might be able to spot the ISS if you look up!')