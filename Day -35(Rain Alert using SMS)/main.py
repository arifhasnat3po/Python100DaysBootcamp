import requests
api_key = "e9c3410f745de30d0aa990ba79db443a"

API = "69f04e4613056b159c2761a9d9e664d2"

# response = requests.get(
#     url="https://api.openweathermap.org/data/2.5/weather?lat=22.42&lon=91.72&appid=e9c3410f745de30d0aa990ba79db443a")
# # https://api.openweathermap.org/data/2.5/weather?lat=22.42&lon=91.72&appid=e9c3410f745de30d0aa990ba79db443a
# lat = 22.423777
# long = 91.723671
# response.raise_for_status()
# data = response.json()
# print(data)

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    'lat': 22.423777,
    'lon': 91.723671,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)

print(response.json())
