# stock-news

Stock news app, written in Python, sending news(and movement in %) about the stock of your choice to your mobile phone using Twilio if the desired stock moves by at least 1%.

This app compares stock prices from yesterday and the day before yesterday.

## Prerequisites
Twilio account  
Twilio library (`pip install twilio`)  
News API account (https://newsapi.org/)  
Alpha Vantage account (http://alphavantage.co/)  
Requirements library (`pip install requirements`)  

## Usage

* First, clone the repo:
```
git clone https://github.com/mclbdn/stock-news
```
* Then, install python packages from requirements.txt:
```
pip install -r requirements.txt
```
* Change the constants and API keys in `main.py`.
* Change the phone numbers to send from and to(according to your Twilio settings) in client.messages.create() in `main.py`.
* Run `python3 main.py`.

## Screenshot

<img src="https://raw.githubusercontent.com/mclbdn/stock-news/main/screenshot.jpeg" width="300" height="600">
