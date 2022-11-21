from lyricsgenius import Genius
from config import ACCESS_TOKEN

genius = Genius(ACCESS_TOKEN)

artist = genius.search_artist(artist_name="1.Cuz", max_songs=3, sort="title")
print(artist.songs)