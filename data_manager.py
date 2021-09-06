import requests

SHEETY_GET = 'https://api.sheety.co/916caf070298948fcad5db9c85a2358c/flightDeals/prices'

class GoogleSheetDataManager:

    @staticmethod
    def get_data_from_sheet():
        response = requests.get(url=SHEETY_GET).json()['prices']
        return response

class GoogleSheetDataRow:

    def __init__(self, city: str, iata_code: str, lowest_price):
        self.city = city
        self.iata_code = iata_code
        self.lowest_price = lowest_price

    @staticmethod
    def create_row_from_raw_data(data_row):
        return GoogleSheetDataRow(
            city=data_row['city'],
            iata_code=data_row['iataCode'],
            lowest_price=data_row['lowestPrice'])