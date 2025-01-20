from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/database"
    db_echo: bool = False


settings = Settings()
