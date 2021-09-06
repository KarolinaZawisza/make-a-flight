import requests
from env import TEQUILA_API_KEY

TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'

headers = {
    'apikey': TEQUILA_API_KEY
}

class FlightSearch:

    @staticmethod
    def search_flights(city_code: str) -> dict:

        params = {
            'fly_from': 'WRO',
            'fly_to': city_code,
            'date_from': '06/09/2021',
            'date_to': '13/09/2021',
            'adults': 1
        }

        response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=params).json()

        return response
