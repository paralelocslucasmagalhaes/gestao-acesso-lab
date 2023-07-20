from typing import List, Union

from pydantic import BaseModel

class CriacaoDepartamento(BaseModel):
    nome: str
    ativo: bool
    
class Departamento(BaseModel):
    id: int
    nome: str
    is_active: bool

    class Config:
        orm_mode = True
