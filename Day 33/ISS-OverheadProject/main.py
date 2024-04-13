import requests
from datetime import datetime
MY_LAT = 32.842080
MY_LNG = -97.012501

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")
sunset = data["results"]["sunset"].split("T")
print(f"sunrise: {sunrise}")
print(f"sunset: {sunset}")

time_now = datetime.now()
print(time_now.hour)