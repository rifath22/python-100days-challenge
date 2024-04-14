from twilio.rest import Client

account_sid = ${{ secrets.ACCOUNT_SID }}
auth_token = ${{ secrets.AUTH_TOKEN }}

client = Client(account_sid, auth_token)

def send(message_body):
    return client.messages \
                    .create(
                        body=message_body,
                        from_='+14146676219',
                        to='+12108129241'
                    )
