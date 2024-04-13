import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from twilio.rest import Client

account_sid = os.getenv('twillio_account_sid')
auth_token = os.getenv('twillio_auth_token')
client = Client(account_sid, auth_token)
class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)
    
    def send_message(self):
        return self.client.messages \
                    .create(
                        body="No need of Umbrella today",
                        from_='+14146676219',
                        to='+12108129241'
                    )