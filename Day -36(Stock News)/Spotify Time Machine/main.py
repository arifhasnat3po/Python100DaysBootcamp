import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "b42bfdf18f984eeb84b93819706290c3"
CLIENT_SECRET = "41c41bc7697a4653ab256c3b5f18435d"
REDIRECT_URI = "http://localhost:8888/callback"  #http://example.com


date = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD ")

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL+date)
print(response)

music_data = response.text

soup = BeautifulSoup(music_data,"html.parser")
# songs = soup.select("li ul li h3")
songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs_titles = [song.getText().strip() for song in songs]
print(songs_titles)



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=REDIRECT_URI,
    client_id= CLIENT_ID,
    client_secret= CLIENT_SECRET,
    show_dialog=False,
    cache_path="token.txt"
    )
    )
try:
    user_id = sp.current_user()["id"]
    print(f"Successfully authenticated as {user_id}")
except spotipy.SpotifyOauthError as e:
    print(f"Authentication error: {e}")
    
song_names = ["The list of song", "titles from your", "web scrape"]

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)






# set SPOTIPY_CLIENT_ID='b42bfdf18f984eeb84b93819706290c3'
# set SPOTIPY_CLIENT_SECRET='41c41bc7697a4653ab256c3b5f18435d'