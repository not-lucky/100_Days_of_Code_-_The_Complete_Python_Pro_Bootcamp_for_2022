import pandas as pd
import smtplib
import random
import datetime as dt

data = pd.read_csv('birthdays.csv')
print(data)

now = dt.datetime.now()
current_date = now.day
current_month = now.month

for (index, row) in data.iterrows():
    if row.month == current_month and row.day == current_date:
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(
            user='rtpoiqw',
            password=
            "'requests', 'clint', 'faker', 'selenium', 'colorama', 'undetected-chromedriver', 'selenium-wire'"
        )

        select_letter = f'letter_templates/letter_{random.randint(1, 3)}.txt' 
        print(select_letter)
        with open(select_letter) as letter:
            raw_letter_content = letter.read()

        personalised_letter = raw_letter_content.replace('[NAME]', row['name'])

        connection.sendmail(
            from_addr="rtpoiqw@gmail.com",
            to_addrs=row.email,
            msg=f"Subject:Happy Birthday\n\n{personalised_letter}")
        connection.close()
