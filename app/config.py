from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

import os

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str
    CLIENT_ORIGIN: str

    model_config = SettingsConfigDict(env_file="./.env")


@lru_cache
def get_settings():
    return Settings() # type: ignore