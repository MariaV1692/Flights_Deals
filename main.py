from dotenv import load_dotenv

load_dotenv()
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import FLIGHTS_SHEETY_SHEET_NAME, FLIGHTS_SHEETY_ENDPOINT, USERS_SHEETY_SHEET_NAME, USERS_SHEETY_ENDPOINT

ORIGIN_CITY = "Tel Aviv"


data_manager = DataManager()

flights_sheet_data = data_manager.getting_data(sheety_endpoint=FLIGHTS_SHEETY_ENDPOINT, sheet_name=FLIGHTS_SHEETY_SHEET_NAME)
users_sheet_data = data_manager.getting_data(sheety_endpoint=USERS_SHEETY_ENDPOINT, sheet_name=USERS_SHEETY_SHEET_NAME)

for city in flights_sheet_data:
    if city["iataCode"] == "":
        flight_search = FlightSearch(city["city"])
        city["iataCode"] = flight_search.getting_iata_code()
        flight_data = flight_search.getting_flights_data(origin_city=ORIGIN_CITY)
        try:
            city["lowestPrice"] = flight_data[0]["price"]
        except:
            continue
        flight_details = FlightData(flight_data)
        if city["lowestPrice"] <= city["wantedPrice"]:
            text_message = flight_details.format_flight_details()
            notification = NotificationManager()
            # notification.send_message(text_message=text_message)
            for user in users_sheet_data:
                notification.send_emails(user=user["email"], message=text_message)

data_manager.updating_data(flights_sheet_data)
