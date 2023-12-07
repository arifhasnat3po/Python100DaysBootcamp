import requests
from twilio.rest import Client

# TODO: Replace with your actual API keys and Twilio credentials
ALPHAVANTAGE_API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
YOUR_PHONE_NUMBER = "YOUR_PHONE_NUMBER"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Get yesterday's and day before yesterday's closing stock prices
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

# Extract yesterday's and day before yesterday's closing prices
dates = list(data.keys())[:2]
yesterday_closing_price = float(data[dates[0]]["4. close"])
day_before_yesterday_closing_price = float(data[dates[1]]["4. close"])

# Calculate the percentage difference
percentage_difference = abs(
    (yesterday_closing_price - day_before_yesterday_closing_price) / day_before_yesterday_closing_price) * 100

# Check if the percentage difference is greater than 5
if percentage_difference > 5:
    # STEP 2: Get the first 3 news pieces for the COMPANY_NAME
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    # STEP 3: Send each article as a separate message via Twilio
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in articles:
        headline = article["title"]
        brief = article["description"]

        # TODO: Format the message if needed
        message = f"{STOCK_NAME}: {'🔺' if yesterday_closing_price > day_before_yesterday_closing_price else '🔻'}{percentage_difference:.2f}%\nHeadline: {headline}\nBrief: {brief}"

        # Send the message via Twilio
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
