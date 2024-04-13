import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
flight_sheety_endpoint = os.getenv('flight_sheety_endpoint')

class FlightData:
    def __init__(self):
        self.response = requests.get(url=flight_sheety_endpoint)
        self.response.raise_for_status()
        self.data = self.response.json()
    
    def check_empty_codes(self, sheet_data):
        for row in sheet_data["prices"]:
            if row['iataCode'] == "":
                row['iataCode'] = "TESTING"
                sheet_inputs  = {
                    'price': row
                }
                # print(row)
                update_sheet_url = f"{flight_sheety_endpoint}/{row['id']}"
                update_pixel_response = requests.put(url=update_sheet_url, json=sheet_inputs)
                update_pixel_response.raise_for_status()
        return True