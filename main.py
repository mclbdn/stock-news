import requests
from twilio.rest import Client

# Stock constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage constants
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = "" # Your Alpha Vantage key

# News Api constants
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NA_API_KEY = "" # Your News API key

# Twilio constants
TWILIO_SID = "" # Your Twilio sid
TWILIO_TOKEN = "" # Your Twilio token

# Process data from Alpha Vantage
av_params = {"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": AV_API_KEY}

av_response = requests.get(STOCK_ENDPOINT, params=av_params)
av_response.raise_for_status()

av_data = av_response.json()["Time Series (Daily)"]

list_of_prices = [value for (key, value) in av_data.items()]

yesterday_price = float(list_of_prices[0]["4. close"])

the_day_before_yesterday_price = float(list_of_prices[1]["4. close"])

difference = yesterday_price - the_day_before_yesterday_price

difference_percent = ((yesterday_price - the_day_before_yesterday_price) / the_day_before_yesterday_price) * 100

# If stock moves by at least 1% in any direction, send 3 articles about given stock
if abs(difference_percent) >= 1:
    print(difference_percent)
    # Process News Api data
    na_params = {"qInTitle": COMPANY_NAME, "apiKey": NA_API_KEY}
    na_response = requests.get(NEWS_ENDPOINT, params=na_params)
    na_response.raise_for_status()

    na_data = na_response.json()["articles"]
    top_three_news = na_data[:3]

    up_down = None

    if difference_percent > 0:
        # Stock moved positively
        up_down = "🔺"
    else:
        # Stock moved negatively
        up_down = "🔻"

    news_to_send = [
        f'{STOCK_NAME} {up_down}{round(difference_percent, 2)}%\nHeadline: {article["title"]}\nBrief: {article["description"]}'
        for article in top_three_news
    ]

    client = Client(TWILIO_SID, TWILIO_TOKEN)

    # Send three text messages
    for single_news in news_to_send:
        # Add your Twilio data
        message = client.messages.create(body=single_news, from_="", to="")
        print(message.status)
