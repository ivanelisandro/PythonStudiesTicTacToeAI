def tracklist(**kwargs):
    for band, albums in kwargs.items():
        print(band)
        for album, song in albums.items():
            print(f"ALBUM: {album} TRACK: {song}")
