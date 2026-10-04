import os
from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

engine = create_engine(os.environ["DATABASE_URL"])
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_db() -> Iterator[Session]:
    # Los endpoints piden la sesión por acá. En los tests se reemplaza con
    # app.dependency_overrides para que usen la sesión de la fixture.
    with SessionLocal() as session:
        yield session
