import os
import requests
from datetime import datetime, timedelta

KIWI_API_KEY = os.environ["KIWI_API_KEY"]
KIWI_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_FLIGHTS_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
    "accept": "application/json"
}


class FlightSearch:
    def __init__(self, city_name):
        self.city = city_name
        self.time_delta = 30 * 6

    def getting_iata_code(self, city=""):
        city_to_check = city if city else self.city
        kiwi_params = {
            "term": city_to_check
        }
        response = requests.get(url=KIWI_LOCATIONS_ENDPOINT, params=kiwi_params, headers=KIWI_HEADERS)
        data = response.json()["locations"]
        for city in data:
            if city["name"].lower() == city_to_check.lower():
                return city["code"]
        return None

    def getting_flights_data(self, origin_city):
        today_date = datetime.today() + timedelta(1)
        today_date_formatted = today_date.strftime("%d/%m/%Y")
        time_frame = today_date + timedelta(self.time_delta)
        time_frame_formatted = time_frame.strftime("%d/%m/%Y")
        kiwi_params = {
            "fly_from": self.getting_iata_code(city=origin_city),
            "fly_to": self.getting_iata_code(),
            "dateFrom": today_date_formatted,
            "dateTo": time_frame_formatted,
            "flight_type": "oneway",
            "curr": "ILS",
            "sort": "price",
            "adults": "1",
            "max_stopovers": "0"
            # "nights_in_dst_from": "3",
            # "nights_in_dst_to": "10"
        }
        response = requests.get(url=KIWI_FLIGHTS_ENDPOINT, headers=KIWI_HEADERS, params=kiwi_params)
        response.raise_for_status()
        return response.json()["data"]
