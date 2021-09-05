from data_manager import DataManager
from flight_data import FlightData

google_sheet_data = []
for row in DataManager.get_gs_data():
    record = DataManager(
        row['city'],
        row['iataCode'],
        row['lowestPrice']
    )
    google_sheet_data.append(record)

flights_api_data = FlightData.get_data_from_API(google_sheet_data)
google_sheet_lowest_prices = FlightData.get_data_from_google_sheet(google_sheet_data)

FlightData.check_flights_prices(google_sheet_data, flights_api_data, google_sheet_lowest_prices)