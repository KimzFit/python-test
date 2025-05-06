from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  title : str
  price : float


@app.get("/")
def read_root():
  return {"Hello" : "World"}

@app.get("/item/{item_id}")
def read_item(item_id : int):
  return {"item_id" : item_id}

@app.put("/item/{item_id}")
def update_item(item : Item , item_id : int):
  return {"item_name" : item.title , "item_id" : item_id}