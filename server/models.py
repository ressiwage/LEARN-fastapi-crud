from pydantic import BaseModel


class Product_model(BaseModel):
    id: int | None = None
    name: str | None = None
    price: float | None = None
    idPhoto: int | None = None


class Customer_model(BaseModel):
    id: int | None = None
    name: str | None = None
    surname: str | None = None
    age: int | None = None
