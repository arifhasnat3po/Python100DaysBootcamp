import requests
import os
from twilio.rest import Client


def get_hourly_forecast(api_key, location_key):
    base_url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"
    endpoint = f"{location_key}?apikey={api_key}"

    try:
        response = requests.get(base_url + endpoint)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching hourly forecast: {e}")
        return None


# Replace 'your_api_key' with your actual AccuWeather API key
api_key = os.environ.get("API_KEY")
location_key = "27728"  # Location key for Pahartali, Chittagong

account_sid = 'ACfc1f22b14a2d1f898ba9959c1f182d5a'
auth_token = os.environ.get("AUTH_TOKEN")


hourly_forecast = get_hourly_forecast(api_key, location_key)

will_rain = False

if hourly_forecast:
    # Print or process the hourly forecast data as needed
    for hour in hourly_forecast:
        # print(
        # f"Time: {hour['DateTime']}, Temperature: {hour['Temperature']['Value']}°C, Condition: {hour['IconPhrase']}")

        if "Rain" in hour['IconPhrase']:
            # print("Rain is expected. Bring an umbrella!")
            will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an Umbrella ☂️",
            from_='',
            to=''
        )

        print(message.status)
