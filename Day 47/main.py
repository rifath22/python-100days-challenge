from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

my_email = os.getenv('my_email')
password = os.getenv('my_email_password')
another_email_address = os.getenv('another_email_address')
# my_email = "azasrifath@gmail.com"
# password = "AzasRifath@2204"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language": 'en-US,en;q=0.9'
}

amazon_instant_pot_url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B07588SJHN/ref=sr_1_4?keywords=instant+pot&qid=1652748310&sprefix=instan%2Caps%2C97&sr=8-4"

amazon_response = requests.get(url=amazon_instant_pot_url, headers=headers)
data = amazon_response.text
# print(data)

soup = BeautifulSoup(data, "lxml")
# price_list = soup.find_all(name="span", class_="reinventPricePriceToPayMargin")
price_list = soup.find_all(name="span", class_="a-offscreen")

buying_prices = [price.getText() for price in price_list]
print(f"buying_prices: {buying_prices}")
# for price in price_list:
#     text = price.getText()
#     print(text)
final_price = float(buying_prices[0].split('$')[1])
print(f"final_price: {final_price}")
expected_price = 165

message_content = f"Instant-Pot-Ultra-Programmable-Sterilizer is now available at {final_price}"

if final_price < expected_price:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=another_email_address, 
                            msg=f"Subject:Amazon Price Tracker\n\n {message_content}")