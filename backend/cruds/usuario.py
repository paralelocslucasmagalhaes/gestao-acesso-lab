from sqlalchemy.orm import Session
from schemas.usuario import CriacaoUsuario
from models.usuario import Usuario as UsuarioDB
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def criar_usuario(db: Session, user: CriacaoUsuario):   

    with tracer.start_as_current_span("salvar_usuario_db"):
        db_user = UsuarioDB(
                            email=user.email, 
                            nome=user.nome,
                            id_departamento = user.id_departamento,
                            is_active = user.ativo
                            )
        db.add(db_user)
        db.commit()  ## EFETIVAR AS TRANSACOES
        db.refresh(db_user)

        return db_user


def get_usuario(db: Session, user_id: int):
    return db.query(UsuarioDB).filter(UsuarioDB.id == user_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    with tracer.start_as_current_span("get_usuario_db"):
        return db.query(UsuarioDB).offset(skip).limit(limit).all()



# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()





# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item