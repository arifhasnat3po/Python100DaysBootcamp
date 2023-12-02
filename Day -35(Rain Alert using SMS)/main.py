import requests
api_key = "e9c3410f745de30d0aa990ba79db443a"

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather?lat=22.42&lon=91.72&appid=e9c3410f745de30d0aa990ba79db443a")
# https://api.openweathermap.org/data/2.5/weather?lat=22.42&lon=91.72&appid=e9c3410f745de30d0aa990ba79db443a
lat = 22.423777
long = 91.723671
response.raise_for_status()
data = response.json()
print(data)
