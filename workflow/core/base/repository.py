from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from workflow.core.base.model import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepositoryMixin(Generic[T]):
    model: T
    async_session: AsyncSession


class BaseAddRepositoryMixin(BaseRepositoryMixin[T]):
    async def add_model_with_async_session(self, model: T, async_session: AsyncSession) -> T:
        async_session.add(model)
        await async_session.flush()
        await async_session.commit()
        return model

    async def add_model(self, model: T) -> T:
        return await self.add_model_with_async_session(model, self.async_session)


class BaseUpdateRepositoryMixin(BaseRepositoryMixin[T]):
    pass


class BaseDeleteRepositoryMixin(BaseRepositoryMixin[T]):
    pass


class BaseRepository(
    BaseAddRepositoryMixin[T],
    BaseUpdateRepositoryMixin[T],
    BaseDeleteRepositoryMixin[T],
):
    def __init__(self, model: T, async_session: AsyncSession):
        self.model = model
        self.async_session = async_session


__all__ = ["BaseRepository"]
