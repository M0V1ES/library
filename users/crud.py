from users.schemas import CreateUser


def create_user(user_in: CreateUser):
    book = user_in.model_dump()
    return {
        "success": True,
        "book": book,
    }
