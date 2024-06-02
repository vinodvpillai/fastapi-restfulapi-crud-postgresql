from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr

class PostBaseSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str

    class Config:
        orm_mode = True


class CreatePostSchema(PostBaseSchema):
    pass


class PostResponse(PostBaseSchema):
    id: uuid.UUID


class UpdatePostSchema(BaseModel):
    title: str
    content: str 
    category: str
    image: str

    class Config:
        orm_mode = True


class ListPostResponse(BaseModel):
    status: str
    results: int
    posts: List[PostResponse]


