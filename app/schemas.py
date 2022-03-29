from pydantic import BaseModel


class Post(BaseModel):
    movie: str
