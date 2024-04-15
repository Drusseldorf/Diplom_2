from typing import List
from pydantic import BaseModel, Field, EmailStr, HttpUrl


class Owner(BaseModel):
    name: str
    email: EmailStr
    createdAt: str
    updatedAt: str


class Ingredient(BaseModel):
    id: str = Field(alias='_id')
    name: str
    type: str
    proteins: int
    fat: int
    carbohydrates: int
    calories: int
    price: int
    image: HttpUrl
    image_mobile: HttpUrl
    image_large: HttpUrl
    v: int = Field(alias='__v')


class Order(BaseModel):
    ingredients: List[Ingredient] | None = None
    id: str | None = Field(alias='_id', default=None)
    owner: Owner | None = None
    status: str | None = None
    name: str | None = None
    createdAt: str | None = None
    updatedAt: str | None = None
    number: int
    price: int | None = None


class MakeOrder(BaseModel):
    success: bool
    message: str | None = None
    name: str | None = None
    order: Order | None = None
    status_code: int
