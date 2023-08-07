from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.usuario import CriacaoUsuario
from schemas.usuario import Usuario
from cruds import usuario as crud_usuario
from core.database import get_db


router = APIRouter()

@router.post("", response_model=Usuario) 
@router.post("/", response_model=Usuario) 
def criar_usuario(usuario: CriacaoUsuario, db: Session = Depends(get_db)):
    response = crud_usuario.criar_usuario(db, usuario)
    return response

@router.get("", response_model=List[Usuario])
@router.get("/", response_model=List[Usuario])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_usuario.get_usuarios(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}/", response_model=Usuario)
@router.get("/{user_id}", response_model=Usuario)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_usuario.get_usuario(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user
