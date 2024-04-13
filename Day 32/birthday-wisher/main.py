import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "azasrifath@gmail.com"
password = "AzasRifath@2204"

data = pd.read_csv("./birthdays.csv")
dict_data = data.to_dict(orient='records')
# print(dict_data)

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


shortlisted_items = [item for item in dict_data if item['day'] == day and item['month'] == month]
print(shortlisted_items)


random_number = random.randint(1,3)
for item in shortlisted_items:
    with open(f'./letter_templates/letter_{random_number}.txt', mode='r') as letter:
        letter_contents = letter.read()
        letter_contents = letter_contents.replace("[NAME]", item['name'])

    # print(letter_contents)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=item['email'], 
                            msg=f"Subject:Birthday wish\n\n {letter_contents}")




