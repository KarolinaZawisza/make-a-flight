from data_manager import GoogleSheetDataManager, GoogleSheetDataRow
from flight_data import FlightData
from notification_manager import NotificationManager
from receivers_manager import ReceiversManager
from date_manager import DateManager

DateManager.get_starting_date()

def get_google_sheet_rows():
    google_sheet_rows_to_return = []
    for data_row in GoogleSheetDataManager.get_data_from_sheet():
        record = GoogleSheetDataRow.create_row_from_raw_data(data_row)
        google_sheet_rows_to_return.append(record)
    return google_sheet_rows_to_return


def get_receivers():
    receivers_data = []
    for row in ReceiversManager.get_receivers_data():
        new_receiver = ReceiversManager.create_row_from_raw_data(row)
        receivers_data.append(new_receiver)
    return receivers_data


def send_emails_to_receivers(receivers):
    for receiver in receivers:
        message = NotificationManager.create_message(receiver.name, notification_list)
        NotificationManager.send_email_notification(message, receiver.email)
        print(f'Sent email to {receiver.name}!')


def send_emails():
    receivers = get_receivers()
    send_emails_to_receivers(receivers)


google_sheet_rows = get_google_sheet_rows()
notification_list = FlightData.obtain_notifications(google_sheet_rows)
send_emails()
