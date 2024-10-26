from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Column, func
from sqlmodel import Field

from workflow.core import BaseSchema


class BaseModel(BaseSchema):
    remove: bool = Field(default=False)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


__all__ = ["BaseModel"]
