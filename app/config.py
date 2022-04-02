from pydantic import BaseSettings


class Settings(BaseSettings):
    API_key: str

    class Config:
        env_file = ".env"


settings = Settings()
