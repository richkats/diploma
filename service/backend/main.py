# -*- coding: utf-8 -*-
from typing import List

from fastapi import Depends, FastAPI, HTTPException

from database import db_manager as db, crud, schemas

app = FastAPI()

sleep_time = 10


async def reset_db_state():
    db.db._state._state.set(db.db_state_default.copy())
    db.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.db.connect()
        yield
    finally:
        if not db.db.is_closed():
            db.db.close()


@app.post("/users/", response_model=schemas.User, dependencies=[Depends(get_db)])
async def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user=user)


@app.get("/users/", response_model=List[schemas.User], dependencies=[Depends(get_db)])
def read_users(skip: int = 0, limit: int = 100):
    users = crud.get_users(skip=skip, limit=limit)
    return users


@app.post("/genres/", response_model=schemas.Genre, dependencies=[Depends(get_db)])
async def create_genre(genre: schemas.GenreCreate):
    db_genre = crud.get_genre_by_name(name=genre.name)
    if db_genre:
        raise HTTPException(status_code=400, detail="Genre already exist")
    return crud.create_genre(genre=genre)


@app.get("/genres/", response_model=List[schemas.Genre], dependencies=[Depends(get_db)])
async def read_genres(skip: int = 0, limit: int = 100):
    genres = crud.get_genres(skip=skip, limit=limit)
    return genres
