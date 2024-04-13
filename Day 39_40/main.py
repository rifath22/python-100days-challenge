#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager, flight_sheety_endpoint
from pprint import pprint
import json
from flight_search import FlightSearch
from datetime import datetime, timedelta

today = datetime.now()
day_of_week = today.weekday()
if day_of_week >= 5:
    today = today - timedelta(2)
print(day_of_week)

tomorrow = today + timedelta(1)
after_six_months = today + timedelta(180)
str_tomorrow = datetime.strftime(tomorrow, '%d/%m/%Y')
str_after_six_months = datetime.strftime(after_six_months, '%d/%m/%Y')

flight_search = FlightSearch()
# flight_data = DataManager(flight_search)
# sheet_data  = flight_data.data
# flight_data.update_airport_codes(sheet_data)
# # pprint(sheet_data)

# for row in sheet_data["prices"]:
#     if row['iataCode'] == "":
#         row['iataCode'] = "TESTING"
#         print(row)
#         update_url = f"{flight_sheety_endpoint}/{row['id']}"
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(sheet_data, f, ensure_ascii=False, indent=4)

with open('data.json', 'r') as f:
    read_data = json.load(f)
#     for row in read_data["prices"]:
#         if row['iataCode'] == "":
#             print(row['city'])
#             tequila_api_data = flight_search.get_iata_code(row['city'])
#             update_code = tequila_api_data['locations'][0]['code']
#             print(f"update_code: {update_code}")
#             check_for_empty_code = flight_data.check_empty_codes(sheet_data, update_code)

    for row in read_data["prices"]:
        fly_to = row['iataCode']
        flight_search.locate_search(fly_to, str_tomorrow, str_after_six_months)
