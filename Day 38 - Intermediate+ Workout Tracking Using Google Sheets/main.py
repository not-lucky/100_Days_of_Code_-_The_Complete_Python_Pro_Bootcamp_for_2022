import requests as req
import datetime as dt
from os import environ

APP_ID = 'df41752a'
API_KEY = 'a3aef085835c5f99e18d2b90147a0d07'

headers = {
    'Content-Type': "application/json",
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

data = {
    "query": "10km cycling",
    "gender": 'male',
    "weight_kg": 74,
    "height_cm": 172,
    "age": 21
}

response = req.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',
                    json=data,
                    headers=headers).json()

current_time = dt.datetime.now()
date = current_time.strftime('%Y/%m/%d')
time = current_time.strftime('%H:%M:%S')

for exercise in response['exercises']:
    sheety_data = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"]
        }
    }
    # print(exercise_list)
    sheety_response = req.post(url=environ['LUCKY_SHEETY_ENDPOINT'],
                               json=sheety_data)
    print(sheety_response.text)
