import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


api_response = requests.get(URL)
empireonline_web_page = api_response.text
soup = BeautifulSoup(empireonline_web_page, 'html.parser')
# print(soup.prettify())
article_header = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in article_header]
reverse_titles = titles[::-1]

with open('movies_list.txt', 'w') as f:
    for line in reverse_titles:
        f.write(line)
        f.write('\n')
