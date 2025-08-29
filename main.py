from fastapi import FastAPI
#from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def greet():
    return("digital world")


@app.get("/products")
def get_all_products():
    return ("all_products")

#class Item(BaseModel):
  # name: str
  #  price: float

#@app.post("/items")
#def create_item(item: Item):
 # return {"name": item.name, "price": item.price}
     

items=[]    

@app.post("/items")
def create_item(item:str):
    items.append(item)
    return items 


