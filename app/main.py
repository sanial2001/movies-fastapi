from fastapi import FastAPI
from . import schemas, get_movies, new_releases

app = FastAPI()


@app.get("/")
def home():
    return {"Home Page"}


@app.post("/predict_movies")
def predict_movies(post: schemas.Post):
    post = post.dict()
    #print(post)
    ans = get_movies.get_movie_recommendation(post['movie'])
    return ans['Title']


@app.get("/get_movies")
def new_movies():
    resp = new_releases.new_release()
    #print(resp)
    return resp
