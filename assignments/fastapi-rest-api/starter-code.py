from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


# Example in-memory data store
items = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build an API", "done": True},
]


class ItemCreate(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: add a GET endpoint to return all items

# TODO: add a GET endpoint to return one item by id

# TODO: add a POST endpoint to create a new item

# TODO: add a PUT or PATCH endpoint to update an item

# TODO: add a DELETE endpoint to remove an item
