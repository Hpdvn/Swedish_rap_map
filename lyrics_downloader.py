import os
import json
from lyricsgenius import Genius
from config import ACCESS_TOKEN

genius = Genius(ACCESS_TOKEN)


def get_artist_lyrics(artist_name, max_songs=10):
    artist = genius.search_artist(artist_name=artist_name, max_songs=max_songs, sort="popularity")
    filename = "Lyrics_" + artist_name + ".json"
    artist.save_lyrics(filename=filename)
    os.replace(filename, "./Lyrics/" + filename)


def get_all_artists(filename="artist_list.json"):
    input_file = open(filename)
    json_array = json.load(input_file)
    return json_array


def get_all_artists_lyrics():
    artists_list = get_all_artists(filename="artist_list.json")
    for artist in artists_list:
        print("Artiste : ", artist)
        get_artist_lyrics(artist_name=artist, max_songs=10)


