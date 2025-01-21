from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from core.models import Author
from .schemas import AuthorCreate, AuthorUpdate


async def get_authors(session: AsyncSession) -> list[Author]:
    stmt = select(Author).order_by(Author.id)
    result: Result = await session.execute(stmt)
    author = result.scalars().all()
    return list(author)


async def get_author(session: AsyncSession, author_id: int) -> Author | None:
    return await session.get(Author, author_id)


async def create_author(session: AsyncSession, author_create: AuthorCreate) -> Author:
    author = Author(**author_create.model_dump())
    session.add(author)
    await session.commit()
    # await session.refresh(book)
    return author


async def update_author(
    session: AsyncSession, author: Author, author_update: AuthorUpdate
) -> Author:
    for name, value in author_update.model_dump(exclude_unset=True).items():
        setattr(author, name, value)
    await session.commit()
    return author


async def delete_book(
    session: AsyncSession,
    author: Author,
) -> None:
    await session.delete(author)
    await session.commit()
