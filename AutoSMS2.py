from twilio.rest import Client

# Set your Twilio account SID and auth token
account_sid = 'ACe2f7af6636ae090441ee770a06fe1d27'
auth_token = 'e1212a6e00247acbdaf7ece526750a84'
client = Client(account_sid, auth_token)

# Set the Twilio phone number to use (must be a Twilio number with SMS capabilities)
from_number = '+16203878221'

# Set the destination phone number (must be in E.164 format)
to_number = '+917019355074'

# Set the message text
message_text = 'Hello, this is a test SMS message from Twilio!'

# Send the message
message = client.messages.create(
    body=message_text,
    from_=from_number,
    to=to_number
)

print(f"Message sent to {to_number} with SID {message.sid}")
