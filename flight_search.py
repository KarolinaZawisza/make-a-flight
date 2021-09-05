import requests

TEQUILA_API_KEY = 'uwxxlYpCHNKC6ea4zPotBPlvBgZM5YMV'
TEQUILA_ENDPOINT = ''

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

        response = requests.get(url='https://tequila-api.kiwi.com/v2/search'
                                , headers=headers, params=params).json()

        return response
