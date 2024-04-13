import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
flight_sheety_endpoint = os.getenv('flight_sheety_endpoint')

class DataManager:
    def __init__(self, flight_search):
        self.flight_search = flight_search
        self.response = requests.get(url=flight_sheety_endpoint)
        self.response.raise_for_status()
        self.data = self.response.json()
    
    def check_empty_codes(self, sheet_data, city, airport_code):
        for row in sheet_data["prices"]:
            if row['iataCode'] == "" and row['city'] == city:
                row['iataCode'] = airport_code
                sheet_inputs  = {
                    'price': row
                }
                print(sheet_inputs)
                update_sheet_url = f"{flight_sheety_endpoint}/{row['id']}"
                update_pixel_response = requests.put(url=update_sheet_url, json=sheet_inputs)
                update_pixel_response.raise_for_status()
        return True
    
    def update_airport_codes(self, sheet_data):
        for row in sheet_data["prices"]:
            if row['iataCode'] == "":
                print(row['city'])
                city_name = row['city']
                tequila_api_data = self.flight_search.get_iata_code(city_name)
                airport_code = tequila_api_data['locations'][0]['code']
                print(f"airport_code: {airport_code}")
                check_for_empty_code = self.check_empty_codes(sheet_data, city_name, airport_code)