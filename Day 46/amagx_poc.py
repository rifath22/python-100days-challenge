import requests
from bs4 import BeautifulSoup

url = 'https://www.saturna.com/amana/growth-fund'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
table = soup.find(id='holdings')

# Print the table
print(table)
