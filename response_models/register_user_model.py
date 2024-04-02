from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    name: str


class RegisterUser(BaseModel):
    success: bool
    message: str = ''
    user: User = None
    accessToken: str = ''
    refreshToken: str = ''
