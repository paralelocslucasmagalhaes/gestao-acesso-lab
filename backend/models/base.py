from typing import List, Union
from datetime import datetime
from pydantic import BaseModel
from pydantic import EmailStr
from uuid import uuid4


class Base(BaseModel):
    id: str = str(uuid4())
    created_date: datetime = datetime.now()
    updated_date: datetime = datetime.now()
    created_by: EmailStr
    updated_by: EmailStr
    active: bool    