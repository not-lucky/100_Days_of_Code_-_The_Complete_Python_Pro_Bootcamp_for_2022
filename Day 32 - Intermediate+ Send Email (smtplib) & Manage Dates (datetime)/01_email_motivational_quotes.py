import smtplib
import datetime as dt
import random
import os

if dt.datetime.now().weekday() == 5:
    with open('quotes.txt') as fl:
        quotes = fl.read().splitlines()

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(
        user='rtpoiqw',
        password=os.environ.get('LUCKY_RTPOIQW_PASS')
    )

    connection.sendmail(
        from_addr="rtpoiqw@gmail.com",
        to_addrs="example@example.com",
        msg=f"Subject:Quotes\n\n{random.choice(quotes)}")
    connection.close()
