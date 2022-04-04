from fastapi import FastAPI
from . import schemas, get_movies, new_releases, find_theatres

app = FastAPI()


@app.get("/")
def home():
    return {"Home Page"}


@app.post("/predict_movies")
def predict_movies(post: schemas.Post_Movies):
    post = post.dict()
    # print(post)
    predicted_movies = get_movies.get_movie_recommendation(post['movie'])
    # print(predicted_movies)
    return predicted_movies['Title']


@app.get("/get_movies")
def new_movies():
    resp = new_releases.new_release()
    return resp


@app.post("/get_nearby_theatres")
def nearby_theatres(post: schemas.Post_Theatres):
    post = post.dict()
    resp = find_theatres.find_nearby_theatres(post['address'])
    return resp
