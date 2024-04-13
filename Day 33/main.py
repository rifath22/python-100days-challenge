import requests
from datetime import datetime
import smtplib
import time
my_email = "azasrifath@gmail.com"
password = "AzasRifath@2204"
MY_LAT = 32.842080
MY_LONG = -97.012501

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_close_to_us = False
#Your position is within +5 or -5 degrees of the ISS position.
if abs(iss_latitude - MY_LAT) <= 5 or abs(MY_LAT - iss_latitude) <= 5 and abs(iss_longitude - MY_LONG) <= 5 or abs(MY_LONG - iss_longitude) <= 5:
    iss_close_to_us = True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    
#If the ISS is close to my current position
    if time_now.hour > sunset and iss_close_to_us:
        print("ISS is close to us")
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="mailmerifath@gmail.com", 
                                msg=f"Subject:Look Up\n\n ISS is close to us")

    time.sleep(10)