import pytest
from fastapi.testclient import TestClient


# El mismo test corre 50 veces. Cada vez arranca con la tabla vacía y deja un
# item creado. Si una corrida viera lo que dejó la anterior, fallaría.
# Además son suficientes tests como para que la diferencia de tiempo entre
# estrategias se note.
@pytest.mark.parametrize("corrida", range(50))
def test_cada_test_arranca_con_la_base_vacia(client: TestClient, corrida: int) -> None:
    assert client.get("/items").json() == []

    response = client.post("/items", json={"name": "siempre-el-mismo", "price": "10"})

    assert response.status_code == 201
