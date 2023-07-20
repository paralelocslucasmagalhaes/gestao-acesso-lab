from fastapi import APIRouter
from api.v1.endpoints import usuario
from api.v1.endpoints import departamento

api_router = APIRouter()
api_router.include_router(usuario.router, prefix="/usuario", tags=["Usuario"])

api_router.include_router(departamento.router, prefix="/departamento", tags=["Departamento"])

