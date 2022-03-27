from twilio.rest import Client
from os import environ


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight) -> None:
        client = Client(environ.get('LUCKY_TWILIO_ACCOUNT_SID'),
                        environ.get('LUCKY_TWILIO_AUTH_TOKEN'))
        client.messages.create(
            to=environ.get('LUCKY_MY_PHONE_NUM'),
            from_=environ.get('LUCKY_TWILIO_PHONE_NUM'),
            body=
            f"Low price alert!\nOnly Rs.{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
