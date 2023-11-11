from pydantic import BaseModel

class Product_model(BaseModel):
    name:str|None = None
    price:float|None = None
    idPhoto:int|None = None