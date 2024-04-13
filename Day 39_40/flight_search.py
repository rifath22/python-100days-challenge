import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
flight_search_endpoint = os.getenv('flight_search_endpoint')
flight_location_search_endpoint = os.getenv('flight_location_search_endpoint')
tequila_API_KEY = os.getenv('tequila_API_KEY')


class FlightSearch:
    def __init__(self):
        self.tequila_params = {
            "term": "Berlin" ,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": True
        }
        self.tequila_headers = {
            "apikey" : tequila_API_KEY,
            "accept": "application/json"
        }
        self.tequila_search_params = {
            "fly_from" : "LHR",
            "fly_to" : "PAR",
            "date_from" : "LHR",
            "date_to" : "LHR",
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type" : "round",
            "curr" : "GBP",
            "max_stopovers" : 0,
            "limit": "1"
        }

    def get_iata_code(self, city_name):
        self.tequila_search_params['term'] = city_name
        tequila_api_response = requests.get(url=flight_search_endpoint, params=self.tequila_params, headers=self.tequila_headers)
        tequila_api_response.raise_for_status()
        tequila_api_data = tequila_api_response.json()
        return tequila_api_data
    
    def locate_search(self, fly_to, date_from, date_to):
        self.tequila_search_params['fly_to'] = fly_to
        self.tequila_search_params['date_from'] = date_from
        self.tequila_search_params['date_to'] = date_to
        # print(self.tequila_search_params)
        tequila_search_api_response = requests.get(url=flight_location_search_endpoint, params=self.tequila_search_params, headers=self.tequila_headers)
        tequila_search_api_response.raise_for_status()
        tequila_api_data = tequila_search_api_response.json()
        print(f"{self.tequila_search_params['fly_to']}: £{tequila_api_data['data'][0]['price']}")
        # return tequila_api_data
