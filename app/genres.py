import pandas as pd

df = pd.read_csv("app/dataset/movie_ratings.csv")
movies_genres = set()
for val in df["genres"]:
    temp = val.split("|")
    for items in temp:
        movies_genres.add(items)

movies_genres = list(movies_genres)
