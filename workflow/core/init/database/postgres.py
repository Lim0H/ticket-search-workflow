from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from workflow.core.config import POSTGRES_SETTINGS

postgres_engine = create_async_engine(
    POSTGRES_SETTINGS.asyncpg_url.unicode_string(),
    future=True,
    echo=True,
)

AsyncSessionFactory = async_sessionmaker(
    postgres_engine,
    autoflush=False,
    expire_on_commit=False,
)


async def get_postgres_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        yield session


__all__ = ["get_postgres_session", "AsyncSessionFactory", "postgres_engine"]
