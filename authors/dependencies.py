from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Author


async def author_by_id(
    author_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Author:
    author = await crud.get_author(session=session, author_id=author_id)
    if author is not None:
        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {author_id} not found!",
    )
