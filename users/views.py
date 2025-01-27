from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from auth import utils as auth_utils
from core.models import db_helper
from users import crud
from users.schemas import UserBase, User, Token

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user(
    user: UserBase,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user_in=user, session=session)


@router.get("/", response_model=list[User])
async def get_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_user(session=session)
