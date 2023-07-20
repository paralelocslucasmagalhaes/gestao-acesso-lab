from sqlalchemy.orm import Session
from schemas.departamento import CriacaoDepartamento
from models.departamento import Departamento

def criar_departamento(db: Session, depto: CriacaoDepartamento):   
    db_depto = Departamento(
                        nome=depto.nome,
                        is_active = depto.ativo
                        )
    db.add(db_depto)
    db.commit()  ## EFETIVAR AS TRANSACOES
    db.refresh(db_depto)
    return db_depto

def get_departamento(db: Session, id_departamento: int):
    return db.query(Departamento).filter(Departamento.id == id_departamento).first()

def get_departamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Departamento).offset(skip).limit(limit).all()

