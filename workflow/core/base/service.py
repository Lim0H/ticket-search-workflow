from typing import Generic, TypeVar

from workflow.core import BaseModel
from workflow.core import BaseRepository

RepoT = TypeVar("RepoT", bound=BaseRepository)
RenT = TypeVar("RenT", bound=BaseModel)


class BaseService(Generic[RepoT, RenT]):
    pass


__all__ = ["BaseService"]
