import os
from twilio.rest import Client

account_sid = "AC7016d23742fe76c7bed711f5c6917841"
auth_token  = "6679863d4171d763690f0635cd22c459"
client = Client(account_sid, auth_token)

call = client.calls.create(to="8177055751",
                           from_="8336083203",
                           twiml='<Response><Say>Hello there. The person says that they are not okay. Please check on them.</Say></Response>')
print(call.sid)
