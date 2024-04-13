import requests
from datetime import datetime, timedelta
from send_message import send

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YCX91J3LWEMRXNYC"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_API_KEY = "3953a46a099e427490bc2b393b400d1d"
NEWS_URL = "https://newsapi.org/v2/everything"


today = datetime.now()
day_of_week = today.weekday()
if day_of_week >= 5:
    today = today - timedelta(2)
print(day_of_week)

yesterday = today - timedelta(1)
type(yesterday)   
str_today = datetime.strftime(today, '%Y-%m-%d')
str_yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
print(f"str_today: {str_today}")

news_parameters = {
    "q": COMPANY_NAME,
    "from": str_today,
    "to": str_today,
    "sortBy": "popularity",
    "searchIn": "title,description",
    "language": "en",
    "pageSize": 3,
    "apiKey": NEWS_API_KEY,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_url = f'{STOCK_URL}?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={STOCK_API_KEY}'
stock_api_response = requests.get(stock_url)
stock_api_response.raise_for_status()
stock_api_data = stock_api_response.json()

print(stock_api_data["Time Series (Daily)"][str_today]["4. close"])
today_closing_price = float(stock_api_data["Time Series (Daily)"][str_today]["4. close"])
yesterday_closing_price = float(stock_api_data["Time Series (Daily)"][str_yesterday]["4. close"])
# print(type(yesterday_closing_price))

def percentage_difference(today_closing_price, yesterday_closing_price):
    percentage_difference  = yesterday_closing_price - today_closing_price
    percentage_change = ( percentage_difference / yesterday_closing_price ) * 100
    return round(percentage_change, 2)
    
percentage_change = percentage_difference(today_closing_price, yesterday_closing_price)

if abs(percentage_change) >= 5:
    if percentage_change > 0:
        direction = "🔺"
    else:
        direction = "🔻"
    # print(f"{STOCK} is {direction} by {percentage_change}")
    # news_url = f'{NEWS_URL}?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={STOCK_API_KEY}'
    news_api_response = requests.get(NEWS_URL, params=news_parameters)
    news_api_response.raise_for_status()
    news_api_data = news_api_response.json()
    # print(f"news_api_data: {news_api_data}")
    for i in range(3):
        title = news_api_data['articles'][i]['title']
        content = news_api_data['articles'][i]['content']
        # print(f"Headline: {title}")
        # print(f"Brief: {content}")
        format_message = f"{STOCK}: {direction} {percentage_change}% \nHeadline: {title} \nBrief: {content}"
        print(format_message)
        send(format_message)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

