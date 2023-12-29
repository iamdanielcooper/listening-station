import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from spotipy_helpers import spotipy_helpers as sp_helpers
from models.Album import Album
from button import *

load_dotenv()

def get_album_details(sp):
    all_playlists = sp.current_user_playlists()['items']
    playlist_id = sp_helpers.get_playlist_by_name(
        all_playlists, 
        os.getenv("PLAYLIST_NAME")
    ) 

    playlist_items = sp.playlist_items(playlist_id)['items']

    albums = []
    max_albums = 5

    for song in playlist_items:

        if len(albums) >= max_albums:
            break;
            
        album_details = sp_helpers.get_song_album(song)

        album = Album(
            album_details['name'], 
            album_details['uri'], 
            album_details['artists'][0]['name'], 
            album_details['images'][0]['url'])
        
        if album not in albums:
            albums.append(album)
    
    return albums

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            redirect_uri=os.getenv("CLIENT_REDIRECT_URI"),
            scope=os.getenv("SCOPE")
            )
        )
    
    button = Button(25, debounce=0.1)
    
    albums = get_album_details(sp)
    
    # Post MVP, this function should display the data in a couple of different ways in a couple of different places. notably, An e-ink display with the info for what albums are loaded, a higher-res display to show the artwork itself.
    sp_helpers.display_album_details(albums)

    # When we integrate the PI we shouldn't need most of this logic, the loop with wait for input from the buttons and determine the source and match it to the corresponding album.

    while True:
        if button.is_pressed():
            print(sp_helpers.get_loading_wording())
            sp.start_playback(os.getenv("DEFAULT_DEVICE_ID"), albums[0].uri)
        else:
            print("no command from button")
            


    # while True:

    #     # TODO: Stop button

    #     user_input = input("What do you want to hear? (enter the number shown next to the album): ")

    #     if user_input == 'exit':
    #         break;
        
    #     elif 0 <= int(user_input) <= len(albums) -1:
    #         print(sp_helpers.get_loading_wording())
    #         sp.start_playback(os.getenv("DEFAULT_DEVICE_ID"), albums[int(user_input)].uri)

    #     else:
    #         print("Invalid input. Please enter a number as shown above. or enter 'exit' to exit")

print("Booting...")
main()
