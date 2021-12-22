class FlightData:
    def __init__(self, flight_data):
        self.price = flight_data[0]["price"]
        self.flight_date = flight_data[0]["local_departure"].split("T")[0].split("-")
        self.fly_to = flight_data[0]["cityTo"]
        self.vac_duration = flight_data[0]["nightsInDest"]
        self.flight_link = flight_data[0]["deep_link"]

    def format_flight_details(self):
        text = f"Wow! it looks like there is a flight to {self.fly_to} on {self.flight_date[2]}/{self.flight_date[1]}/" \
               f"{self.flight_date[0]} for only {self.price}" \
               f" ILS!\nhere is the link for booking: {self.flight_link}"
        return text
