import datetime as dt


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city,
                 destination_airport, out_date, return_date) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = dt.datetime.fromtimestamp(out_date).strftime('%Y/%m/%d')
        self.return_date = dt.datetime.fromtimestamp(return_date).strftime('%Y/%m/%d')
