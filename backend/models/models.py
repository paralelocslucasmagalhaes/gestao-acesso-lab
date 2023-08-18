from models.base import Base
from enum import Enum
from typing import Deque, List, Optional, Tuple

class ApiResourcesEnum(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATH = 'PATH'
    DELETE = 'DELETE'

class ApisModel(Base):
    path: str
    resource: ApiResourcesEnum    
    
class ScopeModel(Base):
    scope: str
    description: str    
    apis: Optional[List[ApisModel]] = []

class ServiceModel(Base):
    host: str
    description: str
    scopes: Optional[List[ScopeModel]] = []
    apis: Optional[List[ApisModel]] = []

class ApplicationoModel(Base):
    name: str
    description: str    
    services: Optional[List[ServiceModel]] = []
    scopes: Optional[List[ScopeModel]] = []