from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello" : "World"}

@app.get("/item/{item_id}")
def read_item(item_id : int):
  return {"item_id" : item_id}