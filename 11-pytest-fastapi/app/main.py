from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db import Base, engine, get_db
from app.models import Item
from app.schemas import ItemCreate, ItemRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Alcanza para el ejercicio. En un proyecto real esto lo hacen las
    # migraciones (Alembic), no el arranque de la app.
    Base.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/items", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)) -> Item:
    item = Item(**payload.model_dump())
    db.add(item)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un item con ese nombre")
    db.refresh(item)
    return item


@app.get("/items", response_model=list[ItemRead])
def list_items(db: Session = Depends(get_db)) -> list[Item]:
    return list(db.scalars(select(Item).order_by(Item.id)))


@app.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    item = db.get(Item, item_id)
    if item is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Item no encontrado")
    return item
