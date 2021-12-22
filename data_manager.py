import os
import requests

SHEETY_AUTH = os.environ["SHEETY_AUTH"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PROJECT_NAAME = os.environ["SHEETY_PROJECT_NAME"]
FLIGHTS_SHEETY_SHEET_NAME = os.environ["FLIGHTS_SHEETY_SHEET_NAME"]
USERS_SHEETY_SHEET_NAME = os.environ["USERS_SHEETY_SHEET_NAME"]
FLIGHTS_SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAAME}/{FLIGHTS_SHEETY_SHEET_NAME}"
USERS_SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAAME}/{USERS_SHEETY_SHEET_NAME}"


class DataManager:
    def __init__(self):
        self.sheety_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SHEETY_AUTH}"
        }

    def getting_data(self, sheety_endpoint, sheet_name):
        response = requests.get(url=sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        data = response.json()[sheet_name]
        return data

    def updating_data(self, sheet_data):
        for city in sheet_data:
            sheety_params = {
                "price": {
                    "iataCode": city["iataCode"],
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(url=f"{FLIGHTS_SHEETY_ENDPOINT}/{city['id']}", json=sheety_params, headers=self.sheety_headers)
