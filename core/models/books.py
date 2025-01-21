from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_book import Issuance


class Book(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    date_publ: Mapped[date] = mapped_column(Date, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    genre: Mapped[str] = mapped_column(String, nullable=False)
    num_of_aval: Mapped[int] = mapped_column(Integer, nullable=False)
    issuances: Mapped[list["Issuance"]] = relationship(back_populates="book")
