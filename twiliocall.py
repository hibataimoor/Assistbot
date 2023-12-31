import os
from twilio.rest import Client

account_sid = "account_sid"
auth_token  = "auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(to="a_number",
                           from_="your_number",
                           twiml='<Response><Say>Hello there. The person says that they are not okay. Please check on them.</Say></Response>')
print(call.sid)
