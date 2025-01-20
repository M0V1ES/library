from datetime import date

from pydantic import BaseModel
from sqlalchemy import String, Text, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column


class CreateBook(BaseModel):
    name: str
    description: str
    date_publ: date
    author: str
    genre: str
    num_of_aval: int