from datetime import date

from pydantic import BaseModel


class IssuanceBase(BaseModel):
    date_issuance: date
    return_date: date
    user_id: int
    book_id: int


class IssuanceCreate(IssuanceBase):
    pass


class Issuance(IssuanceBase):
    id: int
