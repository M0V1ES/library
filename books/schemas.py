from datetime import date
from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    name: str
    description: str
    date_publ: date
    author: str
    genre: str
    num_of_aval: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    name: str | None = None
    description: str | None = None
    date_publ: date | None = None
    author: str | None = None
    genre: str | None = None
    num_of_aval: int | None = None


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
