from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


# class Usuario(Base):
#     __tablename__ = "usuarios"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(50),  unique=True, index=True)
#     nome  = Column(String(50), index=True)
#     id_departamento = Column(Integer, ForeignKey("departamentos.id"))
#     is_active = Column(Boolean, default=True)