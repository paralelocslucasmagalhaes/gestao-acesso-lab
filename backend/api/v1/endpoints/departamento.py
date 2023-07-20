from fastapi import APIRouter, Depends, HTTPException
from cruds import usuario
from sqlalchemy.orm import Session
from typing import List

from schemas.departamento import CriacaoDepartamento
from schemas.departamento import Departamento
from cruds import departamento as crud_departamento
from core.database import SessionLocal, engine, get_db


router = APIRouter(
    dependencies=[Depends(get_db)],)

@router.post("/", response_model=Departamento )
def criar_departamento(
    departamento: CriacaoDepartamento
   , db: Session = Depends(get_db)):
    return crud_departamento.criar_departamento(db, departamento)

@router.get("/", response_model=List[Departamento])
def ler_departamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_departamento.get_departamentos(db, skip=skip, limit=limit)

@router.get("/{id_departamento}", response_model=Departamento)
def ler_departamento(id_departamento: int, db: Session = Depends(get_db)):
    db_departamento = crud_departamento.get_departamento(db, id_departamento=id_departamento)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    return db_departamento