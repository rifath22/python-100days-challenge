import smtplib
import os
import datetime as dt
import random
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

my_email = os.getenv('my_email')
password = os.getenv('my_email_password')
another_email_address = os.getenv('another_email_address')

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

with open('./quotes.txt', mode='r') as file:
    contents = file.readlines()
random_number = random.randint(0, len(contents))
print(contents[random_number])
# date_of_birth = dt.datetime(year=1992, month=4, day=22)
# print(date_of_birth)
if day_of_week == 2:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=another_email_address, 
                            msg=f"Subject:Motivational Quotes\n\n {contents[random_number]}")

