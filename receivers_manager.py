import pandas as pd

class ReceiversManager:

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    @staticmethod
    def get_receivers_data():
        df = pd.read_csv('receivers_data.csv')
        receivers_data = df.values.tolist()
        return receivers_data