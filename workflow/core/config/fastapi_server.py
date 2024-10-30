from pydantic import Field

from workflow.core.base.config import BaseSettings

__all__ = ["FASTAPI_SETTINGS"]


class FastApiSettings(BaseSettings):
    HOST: str = Field(default="localhost")
    PORT: int = Field(default=8000)


FASTAPI_SETTINGS = FastApiSettings()
