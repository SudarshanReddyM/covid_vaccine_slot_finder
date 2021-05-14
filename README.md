# covid_vaccine_slot_finder



Step 1:
  Fork the folder
  
Step 2:
    Changes to be made in find_slot.py
    
    Change following variables
    TWILIO_PHONE_NUMBER = "12345678"            #Give your twilio number. If you don't have one, create it from twilio.com
    
    DIAL_NUMBERS = ["99999999","888888888"]     #Give the list of numbers to be dialled  
    
    #Give the url that can be accessed publicly which says what to talk on a call
    TWIML_INSTRUCTIONS_URL = "https://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"
    
    client = Client("ACxxxxxxxxxxxxx", "yyyyyyyyyyyy") #Give your twilio ACCOUNT SID and AUTH TOKEN respectively
  
Step 2:
  Install python3 on the system.
 
Step 3:
  Give executable permission to the "init.sh" file
  Command to change permission
  chmod +x init.sh
 
Step 4:
  bash init.sh
  
