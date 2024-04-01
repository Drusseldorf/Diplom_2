from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str


class RegisterUserSuccess(BaseModel):
    success: bool
    user: User
    accessToken: str
    refreshToken: str


class RegisterUserFail(BaseModel):
    success: bool
    message: str
