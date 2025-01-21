from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi import FastAPI
from books import router as books_router
from users.views import router as users_router
from authors import router as authors_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=books_router)
app.include_router(router=users_router)
app.include_router(router=authors_router)

if __name__ == "__main__":
    uvicorn.run(app)
