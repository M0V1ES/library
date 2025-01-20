from fastapi import FastAPI, APIRouter
from books.views import router as books_router
from users.views import router as users_router
import uvicorn
app = FastAPI()
app.include_router(books_router)
app.include_router(users_router)
if __name__ == '__main__':
    uvicorn.run(app)

