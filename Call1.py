from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'ACe2f7af6636ae090441ee770a06fe1d27'
auth_token = 'e1212a6e00247acbdaf7ece526750a84'

# Create a Twilio client
client = Client(account_sid, auth_token)

# The phone number to make the call to
to_number = '+917019355074'

# The phone number to make the call from (must be a Twilio number)
from_number = '+16203878221'

# The URL of the recording to play
recording_url = 'https://youtu.be/MBF1mTW4kFY'

# Create the call
call = client.calls.create(
    to=to_number,
    from_=from_number,
    url=recording_url
)

# Print the call SID
print(call.sid)
