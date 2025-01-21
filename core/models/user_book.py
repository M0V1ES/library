from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import String, Text, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .users import User
    from .books import Book


class Issuance(Base):
    date_issuance: Mapped[date] = mapped_column(Date, nullable=False)
    return_date: Mapped[date] = mapped_column(Date, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    user: Mapped["User"] = relationship(back_populates="issuances")
    book: Mapped["Book"] = relationship(back_populates="issuances")
