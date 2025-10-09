import sys
import pathlib
from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool, create_engine

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Backend"
sys.path.insert(0, str(BASE_DIR))

from app.config import settings
from app.database import Base
from app.models import User, Pet, Breed

DATABASE_URL = settings.db_url.replace("asyncpg", "psycopg2")

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata



def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()