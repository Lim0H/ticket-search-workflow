from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime
from sqlmodel import Field

from workflow.core.base.schema import BaseSchema


class BaseModel(BaseSchema):
    remove: bool = Field(default=False)
    created_at: Optional[datetime] = Field(sa_column=Column(DateTime))
    updated_at: Optional[datetime] = Field(sa_column=Column(DateTime))
