import os
from twilio.rest import Client
import smtplib

MY_NUM = os.environ["MY_NUM"]
MY_EMAIL = "grossmaria38@gmail.com"
EMAIL_PASS = os.environ["EMAIL_PASS"]
ACCOUNT_SID = os.environ["TWILIO_SID_KEY"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]


class NotificationManager:
    def __init__(self):
        self.target_num = "+972544301286"

    def send_message(self, text_message):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
                    body=text_message, from_=MY_NUM, to=self.target_num)

    def send_emails(self, user, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # make the connection secure
            connection.login(user=MY_EMAIL, password=EMAIL_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=user, msg=message)
