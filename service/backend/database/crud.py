from . import db_manager as models, schemas


# Users CRUD


def get_user(user_id: int):
    return models.User.filter(models.User.id == user_id).first()


def get_users(skip: int = 0, limit: int = 100):
    return list(models.User.select().offset(skip).limit(limit))


def get_user_by_email(email: str):
    return models.User.filter(models.User.email == email).first()


def create_user(user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db_user.save()
    return db_user


# Genre CRUD


def create_genre(genre: schemas.GenreCreate):
    db_genre = models.Genre(**genre.dict())
    db_genre.save()
    return db_genre


def get_genre(genre_id: int):
    return models.Genre.filter(models.Genre.id == genre_id).first()


def get_genre_by_name(name: str):
    return models.Genre.filter(models.Genre.name == name).first()


def get_genres(skip: int = 0, limit: int = 100):
    return list(models.Genre.select().offset(skip).limit(limit))
