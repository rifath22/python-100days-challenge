import requests
import os
from pprint import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

spotify_Client_ID = os.getenv('spotify_Client_ID')
spotify_Client_Secret = os.getenv('spotify_Client_Secret')
spotify_user_id = os.getenv('spotify_user_id')
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split('-')[0]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

api_response = requests.get(URL)
billboard_web_page = api_response.text
soup = BeautifulSoup(billboard_web_page, 'html.parser')
# print(soup.prettify())
# article_header = soup.find_all(name="h3", id="title-of-a-story")
song_name = soup.select("h3.c-title.a-no-trucate")

titles = [song.getText().strip() for song in song_name]

print(titles)



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_Client_ID,
                                               client_secret=spotify_Client_Secret,
                                               redirect_uri="https://example.com/callback",
                                               scope= "playlist-modify-private"))

results = sp.current_user()["id"]
# print(f"results: {results}")

#curl --request GET \
#   --url 'https://api.spotify.com/v1/search?type=album&include_external=audio' \
#   --header 'Authorization: ' \
#   --header 'Content-Type: application/json'
# results = sp.search(q=titles[0], limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])
# result = sp.search(q=f"track:{titles[0]} year:{year}", type="track")
# pprint(result["tracks"]["items"][0]["uri"])

track_link = []

for title in titles:
    result = sp.search(q=f"track:{title} year:{2020}", type="track")
    track_link.append(result["tracks"]["items"][0]["uri"])
print(track_link)

playlist = sp.user_playlist_create(user=spotify_user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=track_link)