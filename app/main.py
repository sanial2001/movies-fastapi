from fastapi import FastAPI, HTTPException, Response, status
from . import schemas, get_movies, new_releases, find_theatres, genres

app = FastAPI()


@app.get("/")
def home():
    return {"Home Page"}


@app.post("/predict_movies")
def predict_movies(post: schemas.PostMovies):
    post = post.dict()
    # print(post)
    predicted_movies = get_movies.get_movie_recommendation(post['movie'])
    return predicted_movies['Title']


@app.get("/get_movies_genres")
def get_movies_by_genres():
    return genres.movies_genres


@app.get("/get_movies")
def new_movies():
    resp = new_releases.new_release()
    return resp


@app.post("/get_nearby_theatres")
def nearby_theatres(post: schemas.PostTheatres):
    post = post.dict()
    resp = find_theatres.find_nearby_theatres(post['address'])
    return resp
