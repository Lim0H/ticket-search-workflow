from pydantic_settings import BaseSettings as BaseSettingsPydantic
from pydantic_settings import SettingsConfigDict


class BaseSettings(BaseSettingsPydantic):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )


__all__ = ["BaseSettings"]
