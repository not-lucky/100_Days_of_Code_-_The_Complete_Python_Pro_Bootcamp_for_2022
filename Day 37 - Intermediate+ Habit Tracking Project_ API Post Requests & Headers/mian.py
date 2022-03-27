from webbrowser import get
import requests as req
import datetime as dt
from os import environ

TOKEN = environ.get('LUCKY_PIXELA_TOKEN')
print(TOKEN)
# API_URL = 'https://pixe.la/v1/users'
# USERNAME = 'not-lucky'
# GRAPH_ID = 'ropeskipping1'
# graph_endpoint = f'{API_URL}/{USERNAME}/graphs'
# post_pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

# data = {
#     'token': TOKEN,
#     'username': 'not-lucky',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }

# response = req.post(url=API_URL, json=data)
# print(response.text)

# data = {
#     'id': 'ropeskipping1',
#     'name': 'Rope Skipping',
#     'unit': 'minutes',
#     'type': 'float',
#     'color': 'sora',
#     'timezone': 'Asia/Calcutta'
# }

headers = {'X-USER-TOKEN': TOKEN}

# response = req.post(url=graph_endpoint, json=data, headers=headers)
# print(response.text)


# date = f"{dt.datetime.now().year}{dt.datetime.now().month:0>2}{dt.datetime.now().day:0>2}"

# data = {
#     'date': date,
#     'quantity': '12'
# }

# response = req.post(url=post_pixel_endpoint, json=data, headers=headers)
# print(response.text)

# update_pixel = f'{post_pixel_endpoint}/{date}'

# data = {
#     'quantity': '18'
# }

# response = req.delete(url=update_pixel, json=data, headers=headers)
# print(response.text)