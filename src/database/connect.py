from os import environ

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)

from dataclasses import dataclass

from src.database.models import Base


TESTING = environ.get("TEST", "False") == "True"


def get_env_var(env_var: str, test_var: str) -> str:
    return environ.get(test_var if TESTING else env_var)


@dataclass
class Envs:
    name: str = get_env_var("DB_NAME", "DB_NAME_TEST")
    host: str = get_env_var("BD_HOST", "DB_HOST_TEST")
    port: str = get_env_var("DB_PORT", "DB_PORT_TEST")
    user: str = get_env_var("DB_USER", "DB_USER_TEST")
    passwd: str = get_env_var("DB_PASSWD", "DB_PASSWD_TEST")
    database: str = environ.get("DB_URL")


async def get_engine():
    database_url = Envs.database.format(
        user=Envs.user,
        passwd=Envs.passwd,
        host=Envs.host,
        port=Envs.port,
        name=Envs.name,
    )

    return create_async_engine(database_url)


async def create_tables() -> None:
    engine = await get_engine()

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def connect() -> AsyncSession:
    engine = await get_engine()

    async with AsyncSession(engine) as session:
        yield session
