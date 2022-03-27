import requests as req
import datetime as dt
from flight_data import FlightData
from os import environ

TEQUILA_API_KEY = environ['LUCKY_TEQUILA_KIWI_KEY']


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.ENDPOINT = 'https://tequila-api.kiwi.com'
        self.headers = {
            'accept': 'application/json',
            'apikey': TEQUILA_API_KEY,
        }

    def return_IATA_codes(self, city_name: str):

        parameters = {
            'term': city_name,
            'location_types': 'city',
        }

        return req.get(url=f'{self.ENDPOINT}/locations/query',
                       params=parameters,
                       headers=self.headers).json()['locations'][0]['code']

    def search_flight_price(self, iata_code='PAR'):

        now = dt.datetime.now()
        tommorrow = (now + dt.timedelta(days=1)).strftime('%d/%m/%Y')
        in_6_months = (now + dt.timedelta(days=6 * 30)).strftime('%d/%m/%Y')
        # in_7_days = (now + dt.timedelta(days=7)).strftime('%d/%m/%Y')
        # in_28_days = (now + dt.timedelta(days=28)).strftime('%d/%m/%Y')

        parameters = {
            'fly_from': 'DEL',
            'fly_to': iata_code,
            'date_from': tommorrow,
            'date_to': in_6_months,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'curr': 'INR'
        }
        response = req.get(url=f'{self.ENDPOINT}/search',
                           params=parameters,
                           headers=self.headers)
        with open('wtf.txt', 'a') as lf:
            lf.write(response.json())

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {iata_code}.")
            return None

        return FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["dTimeUTC"],
            return_date=data["route"][1]["dTimeUTC"])
