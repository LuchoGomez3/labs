from fastapi.testclient import TestClient
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Item


def test_crea_un_item(client: TestClient) -> None:
    response = client.post("/items", json={"name": "mate", "price": "1500.50"})

    assert response.status_code == 201
    assert response.json() == {"id": response.json()["id"], "name": "mate", "price": "1500.50"}


def test_el_item_creado_queda_en_la_base(client: TestClient, db_session: Session) -> None:
    item_id = client.post("/items", json={"name": "yerba", "price": "3200"}).json()["id"]

    # El test ve lo que commiteó el endpoint porque comparten la conexión.
    assert db_session.get(Item, item_id).name == "yerba"


def test_nombre_duplicado_devuelve_409(client: TestClient, db_session: Session) -> None:
    client.post("/items", json={"name": "termo", "price": "25000"})

    response = client.post("/items", json={"name": "termo", "price": "1"})

    assert response.status_code == 409
    # El rollback() del endpoint volvió al savepoint, no tiró abajo la
    # transacción del test: el primer termo sigue ahí.
    assert db_session.scalar(select(func.count()).select_from(Item)) == 1


def test_item_inexistente_devuelve_404(client: TestClient) -> None:
    assert client.get("/items/999999").status_code == 404


def test_precio_invalido_devuelve_422(client: TestClient) -> None:
    assert client.post("/items", json={"name": "bombilla", "price": "-1"}).status_code == 422
