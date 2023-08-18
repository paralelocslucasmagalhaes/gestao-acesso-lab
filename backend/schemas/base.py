from models.models import ApplicationoModel
from models.models import ServiceModel
from models.models import ScopeModel
from models.models import ApisModel
from models.base import Base
from models.models import ApiResourcesEnum
from enum import Enum


class RequestApplication(Base):
    name: str
    description: str  

class ResponseApplication(ApplicationoModel):
    pass

class RequestServices(Base):
    host: str
    description: str

class ResponseServices(ServiceModel):
    pass

class RequestScope(Base):
    scope: str
    description: str

class ResponseScope(ScopeModel):
    pass

class RequestAPIs(Base):
    path: str
    resource: ApiResourcesEnum

class ResponseAPIs(ApisModel):
    pass