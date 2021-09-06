from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from receivers_manager import ReceiversManager

google_sheet_data = []
for row in DataManager.get_gs_data():
    record = DataManager(
        row['city'],
        row['iataCode'],
        row['lowestPrice'])
    google_sheet_data.append(record)

flights_api_data = FlightData.get_data_from_API(google_sheet_data)
google_sheet_lowest_prices = FlightData.get_data_from_google_sheet(google_sheet_data)

notification_list = FlightData.check_flights_prices(google_sheet_data, flights_api_data, google_sheet_lowest_prices)

receivers_data = []
for row in ReceiversManager.get_receivers_data():
    receiver = ReceiversManager(
        row[0],
        row[1],
        row[2])
    receivers_data.append(receiver)

for receiver in receivers_data:
    message = NotificationManager.create_message(receiver.name, notification_list)
    NotificationManager.send_email_notification(message, receiver.email)
    print(f'Sent email to {receiver.name}!')
