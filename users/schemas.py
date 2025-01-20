from datetime import date
from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    bio: str
    birth: date