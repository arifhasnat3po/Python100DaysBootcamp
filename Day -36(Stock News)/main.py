import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


ALPHAVANTAGE_API_KEY = "1LO3U68K1E6EGGUC"
NEWS_API_KEY = "0a41efe325574bbe9275b054e6a07bec"
TWILIO_ACCOUNT_SID = "ACfc1f22b14a2d1f898ba9959c1f182d5a"
TWILIO_AUTH_TOKEN = "f1feb5b29b3c4ae2c109bd24e7dc9b48"
TWILIO_PHONE_NUMBER = "+15204474959"
YOUR_PHONE_NUMBER = "+8801626702431"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

# print(data)

dates = list(data.keys())[:2]
print(dates)
yesterday_closing_price = float(data[dates[0]]["4. close"])
day_before_yesterday_price = float(data[dates[1]]["4. close"])
print(yesterday_closing_price)
print(day_before_yesterday_price)


percentage_difference = abs(
    (yesterday_closing_price - day_before_yesterday_price)/yesterday_closing_price)*100
print(percentage_difference)

if percentage_difference > .5:
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
        message = f"{STOCK_NAME}: {'🔺' if yesterday_closing_price > day_before_yesterday_price else '🔻'}{percentage_difference:.2f}%\nHeadline: {headline}\nBrief: {brief}"
        print(message)
        # Send the message via Twilio
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
