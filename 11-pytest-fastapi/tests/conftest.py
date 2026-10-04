import os
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from app.db import Base, get_db
from app.main import app

# rollback: el schema se crea una vez y cada test corre en una transacción
#           que se descarta al final.
# recreate: el schema se borra y se vuelve a crear en cada test. Está solo
#           para comparar tiempos.
STRATEGY = os.environ.get("TEST_STRATEGY", "rollback")


@pytest.fixture(scope="session")
def engine() -> Iterator[Engine]:
    engine = create_engine(os.environ["TEST_DATABASE_URL"])
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def db_session(engine: Engine) -> Iterator[Session]:
    if STRATEGY == "recreate":
        yield from _recreate_schema(engine)
    else:
        yield from _rollback_transaction(engine)


def _rollback_transaction(engine: Engine) -> Iterator[Session]:
    connection = engine.connect()
    transaction = connection.begin()
    # Con create_savepoint, cada commit() de la sesión libera un SAVEPOINT y
    # cada rollback() vuelve al último, pero la transacción de afuera queda
    # abierta. El código de la app commitea como en producción y nada se
    # confirma de verdad.
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    yield session
    session.close()
    transaction.rollback()
    connection.close()


def _recreate_schema(engine: Engine) -> Iterator[Session]:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def client(db_session: Session) -> Iterator[TestClient]:
    app.dependency_overrides[get_db] = lambda: db_session
    # Sin el "with", TestClient no corre el lifespan: el schema lo maneja la
    # fixture engine, no la app.
    yield TestClient(app)
    app.dependency_overrides.clear()
