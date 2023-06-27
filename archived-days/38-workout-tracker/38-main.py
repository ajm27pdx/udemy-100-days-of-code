from auth import NUTRIX_API, NUTRIX_APP, SHEETY_TOKEN
import requests
from datetime import datetime

NUTRIX_EX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/3de872ac503b66170c54fede082bbef3/myWorkouts/workouts'
headers = {
    'x-app-id': NUTRIX_APP,
    'x-app-key': NUTRIX_API,
    'x-remote-user-id': '0'
}

user_gender = 'male'
user_weight = 87.0
user_height = 167.0
user_age = 37

user_input = input('Enter your activity:')

nutrix_query = {
    'query': user_input,
    'gender': user_gender,
    'weight_kg': user_weight,
    'height_cm': user_height,
    'age': user_age
}

response = requests.post(url=NUTRIX_EX_ENDPOINT, json=nutrix_query, headers=headers)
user_json = response.json()['exercises'][0]
user_exercise = user_json['name'].title()
user_duration = user_json['duration_min']
user_calories = user_json['nf_calories']

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}

sheety_query = {
    'workout': {
        'date': datetime.today().strftime("%Y-%m-%d"),
        'time': str(datetime.now().strftime("%H:%M")),
        'exercise': user_exercise,
        'duration': user_duration,
        'calories': user_calories
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=sheety_query, headers=sheety_headers)
print(response.text)
