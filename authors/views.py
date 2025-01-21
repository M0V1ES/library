from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from authors import crud
from authors.schemas import Author, AuthorCreate
from core.models import db_helper

router = APIRouter(tags=["authors"])


@router.post("/", response_model=Author)
async def create_author(
    author_in: AuthorCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_author(session=session, book_create=author_in)


@router.get("/", response_model=list[Author])
async def get_authors(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_authors(session=session)


@router.get("/{author_id}/", response_model=Author)
async def get_author(
    author_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    product = await crud.get_author(session=session, author_id=author_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author {author_id} not found!",
    )
