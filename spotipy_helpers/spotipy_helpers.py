import random

def get_song_album(track):
    return track['track']['album']

def get_playlist_by_name(all_playlists, name):
    
    for playlist in all_playlists:
        print(playlist['name'])
        if playlist['name'] == name:
            return playlist['id'];

def display_formatted_album_information(index, album):
    return str(index + 1) + ": " + album.artist + " - " + album.name

def get_loading_wording():
    return random.choice(
        [
            "Rewinding the tape...",
            "Flipping the record...",
            "Changing the CD...",
            "Spinning the vinyl...",
            "Tuning the radio...",
            "Adjusting the frequency...",
            "Checking the cassette...",
            "Setting up the turntable...",
            "Calibrating the equalizer...",
            "Checking the tracklist...",
            "Initializing the audio...",
            "Syncing with the beats...",
            "Fine-tuning the audio...",
            "Mixing the sound...",
            "Searching for the groove...",
            "Checking the amplifier...",
            "Setting the tone...",
            "Syncing with the rhythm...",
            "Preparing the melody...",
            "Finding the right wavelength...",
            "Analyzing the waveform...",
            "Scanning for beats...",
            "Initializing the playback...",
            "Syncing with the music...",
            "Setting the mood...",
            "Dialing in the frequency...",
            "Building the playlist...",
            "Fine-tuning the sound...",
            "Adjusting the tempo...",
            "Calibrating the speakers...",
            "Mixing the audio...",
            "Loading the beats...",
            "Finding the right vibe...",
            "Checking the waveform...",
            "Syncing with the rhythm...",
            "Setting the ambiance...",
            "Configuring the audio...",
            "Optimizing the melody...",
            "Setting the stage...",
            "Preparing the audio journey...",
            "Checking the stereo...",
            "Warming up the sound...",
            "Crafting the sonic experience...",
            "Analyzing the harmonies...",
            "Loading the harmony...",
            "Fine-tuning the pitch...",
            "Arranging the notes...",
            "Configuring the acoustics..."    
        ]
    )
    
def display_album_details(albums):
    for index, album in enumerate(albums):
        display_formatted_album_information(index, album)