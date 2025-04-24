from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    API_KEY: str
    SUBDOMAIN: str

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
