from datetime import date
from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    name: str
    bio: str
    birth: date
    password: str


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    password: str
    email: EmailStr | None = None
    active: bool = True


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
