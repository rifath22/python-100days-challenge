import requests
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC1dcc0a1fedf7f5b3a38240739e1f26ee"
auth_token = "64b8f44ac54e7bf3e7246cd6f7f549a7"
client = Client(account_sid, auth_token)
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
API_Key = 'e3ffa7e841a163c5fbd3ad003fcc648a'
URL = 'https://api.openweathermap.org/data/2.5/onecall'
MY_LAT = 32.842080
MY_LNG = -97.012501

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_Key,
    "exclude": 'current,minutely,daily'
}
response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

weather_ids = [data["hourly"][i]["weather"][0]["id"] for i in range(12)]
# for i in range(12):
#     weather_ids.append(data["hourly"][i]["weather"][0]["id"])

print(weather_ids)
send_message = False
for i in weather_ids:
    if i > 700:
        send_message = True

if send_message:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="No need of Umbrella today",
                        from_='+14146676219',
                        to='+12108129241'
                    )