import requests as req
from os import environ


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.ENDPOINT = environ['LUCKY_SHEETY_FLIGHT_ENDPOINT']

    def get_sheets_data(self):
        return req.get(url=self.ENDPOINT).json()['prices']

    def update_sheet_data(self, a_dict, id):
        update_url = f'{self.ENDPOINT}/{id}'
        # print(update_url)
        a_dict.pop('id')
        update_with_this = {'price': a_dict}
        req.put(url=update_url, json=update_with_this)
        # print(response.text)
