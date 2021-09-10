import pandas as pd


class ReceiversManager:

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    @staticmethod
    def get_receivers_data():
        data_frame = pd.read_csv('receivers_data.csv')
        receivers_data = data_frame.values.tolist()
        return receivers_data

    @staticmethod
    def create_row_from_raw_data(row):
        return ReceiversManager(
            name=row[0],
            surname=row[1],
            email=row[2])
