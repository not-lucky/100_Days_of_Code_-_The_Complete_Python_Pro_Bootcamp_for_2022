from time import sleep
import requests
from datetime import datetime
import smtplib

MY_LAT = 30.225788  # Your latitude
MY_LONG = 78.821855  # Your longitude


def iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude


def sunrise_sunset_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset


def in_pos_and_time():
    iss_latitude, iss_longitude = iss_pos()

    sunrise, sunset = sunrise_sunset_time()
    time_now = datetime.now()

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        if sunset <= time_now.hour or time_now.hour <= sunrise:
            return True

    return False


while True:
    if in_pos_and_time():
        for _ in range(10):
            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(
                user='rtpoiuqw',
                password=
                "'requests', 'clint', 'faker', 'selenium', 'colorama', 'undetected-chromedriver', 'selenium-wire'"
            )
            connection.sendmail(
                from_addr='rtpoiqw@gmail.com',
                to_addrs='ayushrawat801@gmail.com',
                msg='Subject:ISS\n\nLook above! ISS is here!!!!')
            connection.close()

            sleep(30)
    sleep(120)
