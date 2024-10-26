from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, func
from sqlmodel import Field

from workflow.core.base.schema import BaseSchema


class BaseModel(BaseSchema):
    remove: bool = Field(default=False, repr=False)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_type=DateTime,
        sa_column_kwargs={
            "server_default": func.now(),
        },
        nullable=False,
        repr=False,
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_type=DateTime,
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()},
        repr=False,
    )


__all__ = ["BaseModel"]
