from typing import List, Union

from pydantic import BaseModel


class CriacaoUsuario(BaseModel):
    email: str
    nome: str
    id_departamento: int
    ativo: bool

class CriacaoDepartamento(BaseModel):
    nome: str
    ativo: bool

class Usuario(BaseModel):
    id: int
    email: str
    nome: str
    id_departamento: int
    is_active: bool

    class Config:
        orm_mode = True
    
class Departamento(BaseModel):
    id: int
    nome: str
    is_active: bool

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
