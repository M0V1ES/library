from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Book


async def book_by_id(
    book_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Book:
    book = await crud.get_book(session=session, book_id=book_id)
    if book is not None:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {book_id} not found!",
    )
