from datetime import date

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Book(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    date_publ: Mapped[date] = mapped_column(Date, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    genre: Mapped[str] = mapped_column(String, nullable=False)
    num_of_aval: Mapped[int] = mapped_column(Integer, nullable=False)