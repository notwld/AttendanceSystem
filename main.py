from typing import Union
from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class Cat(BaseModel):
    name: str
    age: int
    breed: Union[str, None] = None

test = {
    "name": "salad",
    "age": 1,
    "breed": "snek"
}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/cats/{cat_id}")
async def read_cat(cat_id: int):
    return {"cat_id": cat_id}

@app.get("/cats")
async def create_cat():
    return test


