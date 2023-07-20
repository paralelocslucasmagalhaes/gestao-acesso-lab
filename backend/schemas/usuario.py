from typing import List, Union

from pydantic import BaseModel

class CriacaoUsuario(BaseModel):
    email: str
    nome: str
    id_departamento: int
    ativo: bool

class Usuario(BaseModel):
    id: int
    email: str
    nome: str
    id_departamento: int
    is_active: bool

    class Config:
        orm_mode = True