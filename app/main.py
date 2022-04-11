from fastapi import FastAPI, HTTPException, Response, status
from . import schemas, get_movies, new_releases, find_theatres, genres, movies_feeds, series_feeds

app = FastAPI()


@app.get("/")
def home():
    return {"Home Page"}


@app.post("/predict_movies",)
def predict_movies(post: schemas.PostMovies):
    post = post.dict()
    predicted_movies = get_movies.get_movie_recommendation(post['movie'])
    if predicted_movies.empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movies not found")
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


@app.get("/movies_feed")
def movies_feeds_section():
    resp = movies_feeds.new_movies_feeds()
    return resp


@app.get("/series_feed")
def series_feeds_section():
    resp = series_feeds.new_series_feeds()
    return resp
