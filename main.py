from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi import FastAPI, APIRouter
from books.views import router as books_router
from users.views import router as users_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(books_router)
app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run(app)
