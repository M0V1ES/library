from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from books import crud
from books.dependencies import book_by_id
from books.schemas import Book, BookCreate, BookUpdate
from core.models import db_helper

router = APIRouter(tags=["books"])


@router.post("/", response_model=Book)
async def create_book(
    book_in: BookCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_book(session=session, book_create=book_in)


@router.get("/", response_model=list[Book])
async def get_books(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_books(session=session)


@router.get("/{book_id}/", response_model=Book)
async def get_book(
    book_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    product = await crud.get_book(session=session, book_id=book_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found!",
    )


@router.patch("/{book_id}/")
async def update_book(
    book_update: BookUpdate,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_book(session=session, book=book)
