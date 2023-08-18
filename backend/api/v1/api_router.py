from fastapi import APIRouter
from api.v1.endpoints import application
from api.v1.endpoints import service
from api.v1.endpoints import scope
from api.v1.endpoints import api



api_router = APIRouter()
api_router.include_router(application.router, prefix="/application", tags=["Application"])
api_router.include_router(service.router, prefix="/application", tags=["Services"])
api_router.include_router(scope.router, prefix="/application", tags=["Scopes"])
api_router.include_router(api.router, prefix="/application", tags=["Apis"])


