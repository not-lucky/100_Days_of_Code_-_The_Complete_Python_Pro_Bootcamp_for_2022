import smtplib
import datetime as dt
import random

if dt.datetime.now().weekday() == 5:
    with open('quotes.txt') as fl:
        quotes = fl.read().splitlines()

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(
        user='rtpoiqw',
        password=
        "'requests', 'clint', 'faker', 'selenium', 'colorama', 'undetected-chromedriver', 'selenium-wire'"
    )

    connection.sendmail(
        from_addr="rtpoiqw@gmail.com",
        to_addrs="ayushrawat801@gmail.com",
        msg=f"Subject:Quotes\n\n{random.choice(quotes)}")
    connection.close()
