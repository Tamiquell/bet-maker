import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from settings.config import settings_pg


engine = create_async_engine(settings_pg.dsn)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


metadata = sqlalchemy.MetaData()
Base = declarative_base(metadata=metadata)
