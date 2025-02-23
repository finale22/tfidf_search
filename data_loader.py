import pandas as pd

def load_data():
    data = pd.read_csv("hf://datasets/vishnupriyavr/spotify-million-song-dataset/spotify_millsongdata.csv")
    return data