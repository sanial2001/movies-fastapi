from pydantic import BaseModel


class PostMovies(BaseModel):
    movie: str


class PostTheatres(BaseModel):
    address: str
