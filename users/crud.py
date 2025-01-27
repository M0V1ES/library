import base64

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from auth.utils import hash_password
from core.models import User
from users.schemas import UserBase


async def create_user(session: AsyncSession, user_in: UserBase):
    hashed_password = hash_password(user_in.password)
    user_data = user_in.model_dump()
    user_data["password"] = base64.b64encode(hashed_password).decode("utf-8")
    user = User(**user_data)
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)
