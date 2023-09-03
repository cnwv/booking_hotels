from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import NullPool
from app.config import settings

if settings.MODE == "TEST":
    database_url = settings.test_db_url
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    database_url = settings.db_url
    DATABASE_PARAMS = {}

engine = create_async_engine(database_url, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
