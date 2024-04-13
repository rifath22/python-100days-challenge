from twilio.rest import Client

account_sid = "AC1dcc0a1fedf7f5b3a38240739e1f26ee"
auth_token = "64b8f44ac54e7bf3e7246cd6f7f549a7"

client = Client(account_sid, auth_token)

def send(message_body):
    return client.messages \
                    .create(
                        body=message_body,
                        from_='+14146676219',
                        to='+12108129241'
                    )