from fastapi import FastAPI
from . import schemas, get_movies

app = FastAPI()


@app.get("/")
def home():
    return {"Home Page"}


@app.post("/predict_movies")
def predict_movies(post: schemas.Post):
    post = post.dict()
    # print(post)
    ans = get_movies.get_movie_recommendation(post['movie'])
    return ans['Title']
