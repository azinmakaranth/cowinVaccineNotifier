import requests
from datetime import date,timedelta,datetime
from time import sleep
import winsound

headers = {
    "accept": "application/json", 
    "Accept-Language": "en_US", 
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }   
district_id = "304" # 304 kottayam, 307 ekm
today = date.today() + timedelta(1) # adding a day to today
date=today.strftime("%d-%m-%Y")
pollInterval = 30
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+ district_id + "&date=" + date
print()
print("================Vaccine Finder================")
print()
print(url)
poll = 0
while True :
    poll = poll + 1
    responseDict = requests.get( url, headers=headers).json()
    centersList = responseDict['sessions']
    if not centersList :
        print()
        print(" Poll " + str(poll))
        print(" No centers found")
        sleep(pollInterval)
    else :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print()
        print(" Poll " + str(poll))
        print(" Vaccines are available, time = " + current_time)
        for centerDict in centersList :
            print("  CenterName = " + centerDict['name'] + ", minAge = " + str(centerDict['min_age_limit']) + ", availableCapacity = " + str(centerDict['available_capacity']) + ", vaccine = " + centerDict['vaccine']) 
        i = 0
        while i <= pollInterval : 
            winsound.Beep(440, 500)
            i=i+1

