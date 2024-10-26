import asyncio

from sqlmodel import SQLModel

from workflow.core.init.database.postgres import postgres_engine


def init_database():
    from workflow import model  # noqa

    async def init_models():
        for table in SQLModel.metadata.sorted_tables:
            try:
                created_at, updated_at, remove = (
                    table.columns.get("created_at"),
                    table.columns.get("updated_at"),
                    table.columns.get("remove"),
                )
                table._columns.remove(created_at)
                table._columns.remove(updated_at)
                table._columns.remove(remove)
                table._columns.extend((created_at, updated_at, remove))
            except KeyError:
                pass
        async with postgres_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
            await conn.run_sync(SQLModel.metadata.create_all)

    asyncio.run(init_models())
