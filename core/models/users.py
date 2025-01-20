from datetime import date

from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
class User(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    birth: Mapped[date] = mapped_column(Date, nullable=False)