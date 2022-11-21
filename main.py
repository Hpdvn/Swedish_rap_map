from lyricsgenius import Genius

genius = Genius(secrets.Genius_API_token)
artist = genius.search_artist("1.Cuz", max_songs=3, sort="title")
print(artist.songs)