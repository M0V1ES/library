from contextlib import asynccontextmanager
from auth.jwt_auth import router as jwt_router
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
app.include_router(router=jwt_router)
if __name__ == "__main__":
    uvicorn.run(app)
