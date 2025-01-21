from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .user_book import Issuance


class User(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    birth: Mapped[date] = mapped_column(Date, nullable=False)
    issuances: Mapped[list["Issuance"]] = relationship(back_populates="user")
