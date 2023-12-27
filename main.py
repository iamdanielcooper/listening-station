import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from spotipy_helpers import spotipy_helpers as sp_helpers

load_dotenv()

class Album:
    def __init__(self, name, uri, artist, artwork):
        self.name = name
        self.artist = artist
        self.artwork = artwork
        self.uri = uri

def main(): 

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENT_ID"), 
            client_secret=os.getenv("CLIENT_SECRET"), 
            redirect_uri=os.getenv("CLIENT_REDIRECT_URI"), 
            scope=os.getenv("SCOPE")
            )
        )

    all_playlists = sp.current_user_playlists()['items']
    playlist_id = sp_helpers.getPlaylistIdByName(all_playlists, 'listening_station') 

    tracks = sp.playlist_items(playlist_id)['items']

    albums = []

    for track in tracks:
        album_details = sp_helpers.getTrackAlbum(track)

        album = Album(
            album_details['name'], 
            album_details['uri'], 
            album_details['artists'][0]['name'], 
            album_details['images'][0]['url'])
        albums.append(album)
    
    for index, album in enumerate(albums):
        sp_helpers.displayFormattedAlbumInformation(index, album)

    user_input = 0

    while True:
        user_input = int(input("Enter a number from above: "))

        if 0 <= user_input <= 4:
            print("You entered a valid number. Exiting the loop.")
            break
        else:
            print("Invalid input. Please enter a number between 0 and 4.")


    sp.start_playback(os.getenv("DEFAULT_DEVICE_ID"), albums[user_input].uri)

main()
