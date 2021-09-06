from flight_search import FlightSearch

class FlightData:

    @staticmethod
    def check_flights_prices(google_sheet_data, flights_api_data, google_sheet_lowest_prices):
        notification_list = []
        for index in range(0, len(google_sheet_data)):
            if google_sheet_lowest_prices[index] > flights_api_data[index]:
                notification_message = (f'Flight to: {google_sheet_data[index].city}\n'
                                        f'For: {flights_api_data[index]}€ '
                                        f'({google_sheet_data[index].lowest_price - flights_api_data[index]}'
                                        f'€ cheaper!)\n\n')
                notification_list.append(notification_message)
        return notification_list

    @staticmethod
    def get_data_from_API(google_sheet_data) -> list:
        flights_api_data = []
        for flight in google_sheet_data:
            city_code = flight.iata_code
            flights_api_data.append(FlightSearch.search_flights(city_code)['data'][0]['price'])

        return flights_api_data

    @staticmethod
    def get_data_from_google_sheet(google_sheet_data) -> list:
        google_sheet_lowest_prices = []
        for price in google_sheet_data:
            google_sheet_lowest_prices.append(price.lowest_price)

        return google_sheet_lowest_prices
