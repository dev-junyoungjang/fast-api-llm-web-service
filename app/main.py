from typing import Union
from dto.item import Item

from fastapi import FastAPI

app = FastAPI(
    title="LLM service api",
    description="LLM service api",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str]):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
