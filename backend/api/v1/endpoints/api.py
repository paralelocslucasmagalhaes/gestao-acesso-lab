from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from typing import List
from cruds.apis import APIs
from schemas.base import RequestAPIs
from schemas.base import ResponseAPIs


router = APIRouter()


@router.post("/{application_id}/service/{service_id}/scope/{scope_id}/api/", status_code=status.HTTP_201_CREATED, include_in_schema=False)
@router.post("/{application_id}/service/{service_id}/scope/{scope_id}/api", status_code=status.HTTP_201_CREATED)
def create_api(application_id: str, service_id: str, scope_id: str, api: RequestAPIs):
    apis = APIs(application_id, service_id, scope_id)
    apis.add(api)
    return {"message": "Record created!"}

@router.get("/{application_id}/service/{service_id}/scope/{scope_id}/api/", response_model=List[ResponseAPIs], include_in_schema=False)
@router.get("/{application_id}/service/{service_id}/scope/{scope_id}/api", response_model=List[ResponseAPIs])
def get_apis(application_id: str, service_id: str, scope_id: str, last_document_id: str = None, order_by: str = None,  limit: int = 100):
    apis = APIs(application_id, service_id, scope_id)
    order = "updated_date"
    if order_by:
        order = order_by
    if last_document_id:
        apis.get_next(last_document_id = last_document_id, order_by=order, limit=limit)
    return apis.get_all(order_by=order, limit=limit)

@router.get("/{application_id}/service/{service_id}/scope/{scope_id}/api/{api_id}/",response_model=ResponseAPIs, include_in_schema=False)
@router.get("/{application_id}/service/{service_id}/scope/{scope_id}/api/{api_id}", response_model=ResponseAPIs)
def get_api(application_id: str, service_id: str, scope_id: str, api_id: str):
    apis = APIs(application_id, service_id, scope_id)
    doc_ref = apis.get(api_id)
    if doc_ref is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return doc_ref