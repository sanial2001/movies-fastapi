from pydantic import BaseModel


class Post_Movies(BaseModel):
    movie: str


class Post_Theatres(BaseModel):
    address: str
