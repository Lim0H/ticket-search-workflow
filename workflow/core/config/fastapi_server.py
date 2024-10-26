from workflow.core.base.config import BaseSettings

__all__ = ["FASTAPI_SETTINGS"]


class FastApiSettings(BaseSettings):
    HOST: str
    PORT: int


FASTAPI_SETTINGS = FastApiSettings()
