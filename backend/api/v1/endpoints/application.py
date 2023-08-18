from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from typing import List
from cruds.application import Application
from schemas.base import RequestApplication
from schemas.base import ResponseApplication


router = APIRouter()

app = Application()

@router.post("/", status_code=status.HTTP_201_CREATED, include_in_schema=False)
@router.post("", status_code=status.HTTP_201_CREATED)
def create_application(application: RequestApplication):
    app.add(application)
    return {"message": "Record created!"}

@router.get("/", response_model=List[ResponseApplication], include_in_schema=False)
@router.get("", response_model=List[ResponseApplication])
def get_applications(last_document_id: str = None, order_by: str = None,  limit: int = 100):
    order = "updated_date"
    if order_by:
        order = order_by
    if last_document_id:
        app.get_next(last_document_id = last_document_id, order_by=order, limit=limit)
    return app.get_all(order_by=order, limit=limit)

@router.get("/{application_id}/",response_model=ResponseApplication, include_in_schema=False)
@router.get("/{application_id}", response_model=ResponseApplication)
def get_application(application_id: str):
    doc_ref = app.get(application_id)
    if doc_ref is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return doc_ref