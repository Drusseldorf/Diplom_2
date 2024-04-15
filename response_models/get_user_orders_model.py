from typing import List
from pydantic import BaseModel, Field


class Orders(BaseModel):
    id: str = Field(alias='_id')
    ingredients: List[str]
    status: str
    name: str
    createdAt: str
    updatedAt: str
    number: int


class UserOrders(BaseModel):
    success: bool
    status_code: int
    message: str | None = None
    orders: List[Orders] | None = None
    total: int | None = None
    totalToday: int | None = None
