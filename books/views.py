from fastapi import APIRouter
from books import crud
from books.schemas import CreateBook

router = APIRouter(prefix="/books", tags=["books"])

@router.post('/')
def create_book(book: CreateBook):
    return crud.create_book(book_in=book)