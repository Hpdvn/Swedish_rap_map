import json
import pandas as pd
import os


def extract_lyrics_from_artist(file_path):
    file = open(file_path)
    data = json.load(fp=file)

    my_df = pd.DataFrame(columns=["artist", "title", "lyrics"])

    for dic in data.get('songs'):
        my_df.loc[len(my_df.index)] = ([dic["artist"], dic["title"], dic["lyrics"]])

    return my_df


def extract_all_artist():
    my_df = pd.DataFrame(columns=["artist", "title", "lyrics"])
    for file in os.listdir("Lyrics"):
        new_df = extract_lyrics_from_artist("Lyrics/" + file)
        my_df = pd.concat([my_df, new_df])
    return my_df

