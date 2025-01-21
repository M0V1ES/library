from datetime import date

from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Author(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True, default="", server_default="")
    birth: Mapped[date] = mapped_column(Date, nullable=False)
