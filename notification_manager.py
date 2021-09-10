import smtplib
from env import MAIN_EMAIL, MAIN_EMAIL_PASSWORD


class NotificationManager:

    @staticmethod
    def create_message(receiver_name, notification_message: list):
        flights_information = ' '.join(notification_message)
        message = f'SUBJECT: Cheaper flight found!\n' \
                  f'Hello {receiver_name}!\n\n' \
                  f'We found the following flights to be cheaper!' \
                  f'{flights_information}\n\n' \
                  f'Don\' miss out on this amazing occasion!\n' \
                  f'Thanks for subscribing to our service!\n' \
                  f'(Tax for your soul will come in mail)\n'

        return message

    @staticmethod
    def send_email_notification(message: str, receiver_email):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MAIN_EMAIL, password=MAIN_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MAIN_EMAIL,
                                to_addrs=receiver_email,
                                msg=message.encode('utf-8')
                                )