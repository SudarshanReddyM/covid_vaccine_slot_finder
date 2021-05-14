import requests
import datetime
import json
import time
from twilio.rest import Client
import logging

log_formatter ='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG, filename="vaccine_slot_finder.log", format=log_formatter)
logging.debug('This will get logged')

# My twilio number which makes calls
TWILIO_PHONE_NUMBER = "+19192308789"

# list of one or more phone numbers to dial
DIAL_NUMBERS = ["+919980205616"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = "https://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"


# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = Client("ACf6e24dd20b02c6120bd359b11b919b58", "c9ad0a435a0a314b96e76a0f5ee35a1c")

# Function that calls the given numbers to notify
def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


district_id = 294 # BBMP district code
today_date =  datetime.date.today().strftime('%d-%m-%Y')
count = 0
# API to get the vaccine centres in the given district_id
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"}
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(str(district_id), str(today_date)) 
print("\n")
while True:
    logging.info("You will receive a call if a vacant slot is found")
    vaccine_centres = requests.get(url=url, headers=headers)
    if vaccine_centres.status_code == 200:
        vaccine_centres = json.loads(vaccine_centres.content.decode("utf-8"))
        print(vaccine_centres)
        for centre in vaccine_centres.get("centers"):
            if count == 1:
                count = 0
                time.sleep(60)
                break
            for session in centre.get("sessions"):      
                if session.get("min_age_limit") == 18 and session.get("available_capacity"):
                    logging.info("Calling and Notifying user")
                    dial_numbers(DIAL_NUMBERS)
                    count = 1
                    break
    else:
        time.sleep(10)
                      