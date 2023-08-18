from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from typing import List
from cruds.services import Services
from schemas.base import RequestServices
from schemas.base import ResponseServices


router = APIRouter()


@router.post("/{application_id}/service/", status_code=status.HTTP_201_CREATED, include_in_schema=False)
@router.post("/{application_id}/service", status_code=status.HTTP_201_CREATED)
def create_service(application_id: str, service: RequestServices):
    services = Services(application_id)
    services.add(service)
    return {"message": "Record created!"}

@router.get("/{application_id}/service/", response_model=List[ResponseServices], include_in_schema=False)
@router.get("/{application_id}/service", response_model=List[ResponseServices])
def get_services(application_id: str, last_document_id: str = None, order_by: str = None,  limit: int = 100):
    services = Services(application_id)
    order = "updated_date"
    if order_by:
        order = order_by
    if last_document_id:
        services.get_next(last_document_id = last_document_id, order_by=order, limit=limit)
    return services.get_all(order_by=order, limit=limit)

@router.get("/{application_id}/service/{service_id}/",response_model=ResponseServices, include_in_schema=False)
@router.get("/{application_id}/service/{service_id}", response_model=ResponseServices)
def get_service(application_id: str, service_id: str):
    services = Services(application_id)
    doc_ref = services.get(service_id)
    if doc_ref is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return doc_ref