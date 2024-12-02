import pywhatkit as kit
import datetime

# Replace 'your_phone_number' with the recipient's phone number (including country code)
phone_number = "+917019355074"

# Set the time for sending the message
now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 1  # Send the message 1 minute from now

# Message content
message = "Hello, this is a test message from pywhatkit!"

# Send the WhatsApp message
kit.sendwhatmsg(phone_number, message, hours, minutes)

print(f"Message will be sent to {phone_number} at {hours}:{minutes}")
