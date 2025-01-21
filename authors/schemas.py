from datetime import date

from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str
    bio: str
    birth: date


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    class AuthorBase(BaseModel):
        name: str | None = None
        bio: str | None = None
        birth: date | None = None


class Author(AuthorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
