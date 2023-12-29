class Album:
    def __init__(self, name, uri, artist, artwork):
        self.name = name
        self.artist = artist
        self.artwork = artwork
        self.uri = uri

    def __eq__(self, other):
        return (
            isinstance(other, Album) and
            self.name == other.name and
            self.uri == other.uri and
            self.artist == other.artist and
            self.name == other.name
        )