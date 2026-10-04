# 11 · pytest + FastAPI

## Pregunta de partida

¿Cómo testeo endpoints FastAPI que tocan Postgres sin recrear la base en cada test?

## Cómo correrlo

Correr los tests (levanta Postgres solo):

```bash
docker compose run --rm tests
```

Correr los mismos tests recreando el schema en cada test, para comparar tiempos:

```bash
TEST_STRATEGY=recreate docker compose run --rm tests
```

Levantar la API para probarla a mano (queda en `http://localhost:8011/docs`):

```bash
docker compose up api
```

Apagar todo y borrar los datos:

```bash
docker compose down -v
```

### Qué hay en cada archivo

| Archivo | Qué hace |
|---|---|
| `app/main.py` | Tres endpoints de items. Crear un item con nombre repetido devuelve 409. |
| `app/db.py` | El engine y `get_db`, la dependencia que los tests reemplazan. |
| `tests/conftest.py` | Lo central del ejercicio: las fixtures `engine`, `db_session` y `client`. |
| `tests/test_items.py` | Tests de los endpoints, incluido el 409 que hace rollback adentro del test. |
| `tests/test_aislamiento.py` | El mismo test 50 veces: cada corrida espera la tabla vacía. |
| `initdb/` | Crea la base `labs_test`, separada de la que usa la API. |

## Qué me llevé

Pendiente.
