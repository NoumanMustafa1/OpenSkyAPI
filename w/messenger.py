import pywhatkit

# The hour and minute at which you want to send the message (in 24-hour format)
hour = 22
minute = 43

# The phone number you want to send the message to, including the country code
to_number = "+17655137961"

# The message text
message_text = "Hello, this is a test message from Nouman."

# Send the message
for i in range(20):
    # pywhatkit.sendwhatmsg(hour, minute, to_number, message_text)
    pywhatkit.sendwhatmsg_instantly(to_number, message_text)
    print(i)
