def getTrackAlbum(track):
    return track['track']['album']

def getPlaylistIdByName(all_playlists, name):
    
    for playlist in all_playlists:
        print(playlist['name'])
        if playlist['name'] == name:
            return playlist['id'];

def displayFormattedAlbumInformation(index, album):
    print(str(index) + ": " + album.artist + " - " + album.name)