import os
import requests as req
from twilio.rest import Client
# import pprint

# print(os.environ.get('MY_PHONE_NUM'))
# print(os.environ.get('LUCKY_TWILIO_PHONE_NUM'))
# print(os.environ.get('LUCKY_MY_PHONE_NUM'))

parameters = {
    'lat': os.environ.get('LUCKY_LAT'),
    'lon': os.environ.get('LUCKY_LONG'),
    'appid': 'fcb6a81bd3d3f08817079dc7ac10825b',
    'units': 'metric',
    'exclude': 'current,minutely,daily',
}

response = req.get(url='https://api.openweathermap.org/data/2.5/onecall',
                   params=parameters)
response.raise_for_status()


def need_umbrella():
    for id in response.json()['hourly'][:12]:
        if int(id['weather'][0]['id']) < 700:
            return True

    return False


# print(response.json()['hourly'][0]['weather'][0]['id'])

account_SID = os.environ.get('LUCKY_TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('LUCKY_TWILIO_AUTH_TOKEN')

if not need_umbrella():
    client = Client(account_SID, auth_token)
    message = client.messages.create(
        body="It's gonna rain today.\nBring and umbrealla ☂️",
        from_=os.environ.get('LUCKY_TWILIO_PHONE_NUM'),
        to=os.environ.get('LUCKY_MY_PHONE_NUM'))
