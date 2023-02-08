import os
from twilio.rest import Client

twilio_account_sid = os.getenv("twilio_account_sid")
twilio_auth_token = os.getenv("twilio_auth_token")
twilio_phone_number = os.getenv("twilio_phone_number")


class Messenger:
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)

    #Send SMS details of stock difference and stock news via twilio api
    def send_sms(self, stock_name, stock_symbol, stock_percentage, headline, brief):
        message = self.client.messages.create(from_=twilio_phone_number,
                                              to="Your Phone number verified with Twilio",
                                              body=f"{stock_name}: {stock_symbol}{stock_percentage}%\n\n"
                                                   f"Headline: {headline}\n\n"
                                                   f"Brief: {brief}")
