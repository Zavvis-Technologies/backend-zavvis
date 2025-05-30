from pydantic_settings import BaseSettings


from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")
    SECRET_KEY: str = Field(...)
    REFRESH_SECRET_KEY: str = Field(...)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30)

    class Config:
        env_file = ".env"

settings = Settings()