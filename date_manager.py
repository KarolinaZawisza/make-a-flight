import datetime


class DateManager:

    @staticmethod
    def get_starting_date():
        starting_date = datetime.datetime.now().strftime('%d/%m/%Y')
        return starting_date

    @staticmethod
    def get_ending_date():
        month = datetime.datetime.now().month + 2
        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        if month + 2 < 12:
            month = (month + 2) - 12
            return f'{day}/{month}/{year + 1}'
        else:
            return f'{day}/{month}/{year}'
