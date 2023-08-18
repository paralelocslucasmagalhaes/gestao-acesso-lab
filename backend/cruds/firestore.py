from google.cloud import firestore
from models.base import Base
from datetime import datetime
from typing import List
import os

PROJECT_ID = os.getenv("PROJECT_ID")

class FirestoreAPI():

    def __init__(self, collection) -> None:
        self.fcli = firestore.Client(project=PROJECT_ID)
        self.collection = collection
        pass

    def get_collection_ref(self):
        return self.fcli.collection(self.collection)

    def get_document_ref(self, document: str):
        return self.fcli.collection(self.collection).document(document)

    def get(self,  document: str):
        return self.get_document_ref(document).get().to_dict()
    
    def get_all(self,  order_by: str = 'updated_date', limit: int = 100):
        # [START firestore_query_cursor_pagination]
        ref = self.get_collection_ref()
        docs = ref.order_by(order_by).limit(limit).stream()
        return [doc.to_dict() for doc in docs]            
    
    def get_next(self,  last_document_id: str, order_by: str = 'updated_date', limit: int = 100):
        ref = self.get_collection_ref()
        docs = ref.order_by(order_by).start_after({"id": last_document_id}).limit(limit)
        return [doc.to_dict() for doc in docs]
    
    def add(self, data: Base):
        return self.fcli.collection(self.collection).document(str(data.id)).set(data.dict())
    
    def add_array(self,  document: str, field: str, data:dict = {}):
        ref = self.get_document_ref(document)
        return ref.update({field: firestore.ArrayUnion([data])})
    
    def add_batch(self, batch, document: str, data: Base):
        ref = self.get_document_ref(document)
        return batch.set(ref, data.dict())
    
    def add_batch_array(self, batch, document: str, field: str, data:dict= {}):
        ref = self.get_document_ref(document)
        items = ref.get().to_dict().get(field, [])
        [batch.update(ref, {field: firestore.ArrayRemove([item])})  for item in items if data.get('id') == item.get('id')]
        return batch.update(ref, {field: firestore.ArrayUnion([data])})
    
    def delete(self,  document: str):
        return self.fcli.collection(self.collection).document(document).delete()

    def update(self, collection: str, document: str, data:Base):
        data.updated_date = datetime.now()        
        return self.get_document_ref(collection, document).set(data.dict())

    def activate(self, collection: str, document: str):
        ref = super().get_document_ref(collection, document)
        return ref.set({"activate": True})
    
    def deactivate(self,  collection: str, document: str):
        ref = super().get_document_ref(collection, document)
        return ref.set({"activate": False})

    def update_array(self, new_value: dict, document: dict, field:list):
        array = document.get(field, [])
        maps = array.copy()
        [maps.pop(index) for index in range(0, len(array)) if new_value.get('id') == array[index].get('id')]
        maps.append(new_value)
        return maps