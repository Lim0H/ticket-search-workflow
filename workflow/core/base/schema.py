from sqlmodel import SQLModel


class BaseSchema(SQLModel):
    pass


__all__ = ["BaseSchema"]
