import requests
from twilio.rest import Client
import time


def get_weather_data(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def is_extreme_weather(weather_data):
    if "main" in weather_data:
        temp = weather_data["main"].get("temp")
        if temp is not None:
            # Define your extreme temperature thresholds
            extreme_high_temp = 35  # Adjust as needed
            extreme_low_temp = 0    # Adjust as needed

            return temp > extreme_high_temp or temp < extreme_low_temp

    return False


def send_sms_alert(account_sid, auth_token, to_phone, from_phone, message):
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message,
            from_=from_phone,
            to=to_phone
        )
        print(f"SMS sent: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")


# Replace these variables with your actual values
api_key = ""
latitude = 22.42
longitude = 91.72

# Twilio credentials
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"
to_phone = "+1234567890"  # Your phone number
from_phone = "+0987654321"  # Your Twilio phone number

while True:
    weather_data = get_weather_data(api_key, latitude, longitude)

    if weather_data and is_extreme_weather(weather_data):
        send_sms_alert(account_sid, auth_token, to_phone,
                       from_phone, "Extreme weather conditions detected!")
        # You might want to add a delay or exit the loop to avoid continuous alerts

    # Check every 5 minutes (adjust as needed)
    time.sleep(300)
