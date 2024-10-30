from asyncio import current_task

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_scoped_session,
    async_sessionmaker,
)
from sqlalchemy.orm import sessionmaker

from workflow.core.config import POSTGRES_SETTINGS

postgres_engine = create_async_engine(
    POSTGRES_SETTINGS.asyncpg_url.unicode_string(),
    future=True,
    echo=False,
)

postgres_engine_sync = create_engine(
    POSTGRES_SETTINGS.postgres_url.unicode_string(),
    future=True,
    echo=False,
)

SessionFactory = sessionmaker(
    postgres_engine_sync,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
AsyncSessionFactory = async_sessionmaker(
    postgres_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

sc_postgres_session = async_scoped_session(
    AsyncSessionFactory, scopefunc=current_task
)

__all__ = ["sc_postgres_session"]
