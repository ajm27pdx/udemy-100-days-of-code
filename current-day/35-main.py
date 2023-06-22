from data import weather_data

hourly_data = weather_data['hourly'][:12]

for hour in hourly_data:
    if hour['weather'][0]['id'] < 700:
        print('umbrella')
