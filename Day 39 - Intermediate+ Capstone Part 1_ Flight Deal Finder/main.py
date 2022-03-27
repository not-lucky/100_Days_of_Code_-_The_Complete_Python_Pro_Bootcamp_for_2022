# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheets_data()

# pprint(sheet_data)

# get iatacode and update sheet with it

for dic in sheet_data:
    if dic['iataCode'] == '':
        dic['iataCode'] = flight_search.return_IATA_codes(
            city_name=dic['city'])

    data_manager.update_sheet_data(dic, dic['id'])

    flight = flight_search.search_flight_price(dic['iataCode'])
    if flight is not None:
        if flight.price < dic['lowestPrice']:
            lol = NotificationManager(flight)
