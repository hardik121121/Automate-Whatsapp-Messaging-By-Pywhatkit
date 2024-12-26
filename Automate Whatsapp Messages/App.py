# pip install pywhatkit

import pywhatkit
import pywhatkit
import datetime

# Get the current time
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute + 1  # Set it to 1 minute ahead

pywhatkit.sendwhatmsg("+917488343926", "Don't Worry Bhai this is an automated whatsapp message by my bot , testing it!", hour, minute)
pywhatkit.sendwhatmsg("+917488343926", "If u recieved it, it means its working fine!", hour, minute+1)
pywhatkit.sendwhatmsg("+917488343926", "Working fine!", hour, minute+2)