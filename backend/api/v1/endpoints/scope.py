from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from typing import List
from cruds.scope import Scopes
from schemas.base import RequestScope
from schemas.base import ResponseScope


router = APIRouter()


@router.post("/{application_id}/service/{service_id}/scope/", status_code=status.HTTP_201_CREATED, include_in_schema=False)
@router.post("/{application_id}/service/{service_id}/scope", status_code=status.HTTP_201_CREATED)
def create_scope(application_id: str, service_id: str, scope: RequestScope):
    scopes = Scopes(application_id, service_id)
    scopes.add(scope)
    return {"message": "Record created!"}

@router.get("/{application_id}/service/{service_id}/scope/", response_model=List[ResponseScope], include_in_schema=False)
@router.get("/{application_id}/service/{service_id}/scope", response_model=List[ResponseScope])
def get_scopes(application_id: str, service_id: str, last_document_id: str = None, order_by: str = None,  limit: int = 100):
    scopes = Scopes(application_id, service_id)
    order = "updated_date"
    if order_by:
        order = order_by
    if last_document_id:
        scopes.get_next(last_document_id = last_document_id, order_by=order, limit=limit)
    return scopes.get_all(order_by=order, limit=limit)

@router.get("/{application_id}/service/{service_id}/scope/{scope_id}/",response_model=ResponseScope, include_in_schema=False)
@router.get("/{application_id}/service/{service_id}/scope/{scope_id}", response_model=ResponseScope)
def get_scope(application_id: str, service_id: str, scode_id: str):
    scopes = Scopes(application_id, service_id)
    doc_ref = scopes.get(scode_id)
    if doc_ref is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return doc_ref