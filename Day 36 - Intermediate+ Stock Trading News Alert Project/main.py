import requests as req
from twilio.rest import Client
from os import environ

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_KEY = 'NGNAKFUV7CF86CXQ'
NEWSAPI_KEY = '083476a9e8f44f34870cc71a725cc3ba'

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': ALPHAVANTAGE_KEY,
}

response = req.get(url='https://www.alphavantage.co/query', params=parameters)
data = response.json()['Time Series (Daily)']
# print(response.json())

close_prices = []
loops_ran = 1
for key, value in data.items():
    if loops_ran < 3:
        close_prices.append(value['4. close'])
        loops_ran += 1
    else:
        break
# print(close_prices)

percentage_changed = ((float(close_prices[0]) - float(close_prices[1])) /
                      float(close_prices[0])) * 100
# print(percentage_changed)

if abs(percentage_changed) >= 3:
    if percentage_changed > 0:
        stock_symbol = '🔺'
    else:
        stock_symbol = '🔻'

    parameters = {
        'apikey': NEWSAPI_KEY,
        'q': COMPANY_NAME,
        'language': 'en',
        'sortBy': 'relevancy',
        'pagesize': 10,
    }

    response = req.get(url='https://newsapi.org/v2/everything',
                       params=parameters).json()
    data = response['articles']

    for article in data[:3]:
        print(article['title'])

        client = Client(environ.get('LUCKY_TWILIO_ACCOUNT_SID'),
                        environ.get('LUCKY_TWILIO_AUTH_TOKEN'))
        message = client.messages.create(
            to=environ.get('LUCKY_MY_PHONE_NUM'),
            from_=environ.get('LUCKY_TWILIO_PHONE_NUM'),
            body=
            f"{STOCK}: {stock_symbol}{round(abs(percentage_changed), 3)}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        )
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
