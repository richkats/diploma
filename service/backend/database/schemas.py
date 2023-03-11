# -*- coding: utf-8 -*-
from typing import Any, List, Union

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


# User models


class UserBase(BaseModel):
    first_name: str
    last_name: str
    nickname: str
    email: str
    photo: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# Genre models


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
