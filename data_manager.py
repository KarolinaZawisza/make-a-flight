import requests

SHEETY_GET = 'https://api.sheety.co/916caf070298948fcad5db9c85a2358c/flightDeals/prices'

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, city: str, iata_code: str, lowest_price):
        self.city = city
        self.iata_code = iata_code
        self.lowest_price = lowest_price

    @staticmethod
    def get_gs_data():
        response = requests.get(url=SHEETY_GET).json()['prices']
        return response