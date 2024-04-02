from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str


class ChangeUser(BaseModel):
    success: bool
    message: str | None = None
    user: User = None
