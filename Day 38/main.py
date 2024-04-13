import requests
import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

today = datetime.now()
str_day = datetime.strftime(today, '%Y/%m/%d')
str_time = datetime.strftime(today, '%H:%M:%S')

print(f"str_day: {type(str_day)}")
print(f"str_time: {type(str_time)}")
nutrionix_API_key = os.getenv('nutrionix_API_key')
nutrionix_Application_ID = os.getenv('nutrionix_Application_ID')
sheety_token = os.getenv('sheety_token')
headers = {
    "Content-Type": "application/json",
    "x-app-id": nutrionix_Application_ID,
    "x-app-key": nutrionix_API_key
}
params = {
 "query":input("Tell me which exercise you did: "),
 "gender":"male",
 "weight_kg":62.5,
 "height_cm":167.64,
 "age":30
}
nutrionix_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"

nutrionix_response = requests.post(url=nutrionix_endpoint, json=params, headers=headers)
data = nutrionix_response.json()
# print(data)
sheety_endpoint = os.getenv('sheety_endpoint')
# resp = requests.get(url=sheety_endpoint)
# resp.raise_for_status()
# print(resp.json())
# output = []

sheety_headers = {"Authorization": sheety_token}
for exercise in data["exercises"]:
    sheet_inputs  = {
        'workout': {
            "date": str_day ,
            "time": str_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
    sheet_response.raise_for_status()

