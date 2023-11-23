import requests
from datetime import datetime
MY_lati = 21.346178
My_long = 91.793287
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(data)
# print(iss_position)
parameters = {
    # "lat": MY_lati,
    # "lng": My_long,
    "formatted": 0
}
# params=parameters
response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
time_now = datetime.now()


print(time_now.hour)
print(sunrise)
# print(data)
print(sunset)
