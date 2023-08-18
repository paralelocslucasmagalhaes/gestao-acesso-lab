
from typing import List
from cruds.firestore import FirestoreAPI
from models.models import ServiceModel
from cruds.application  import Application

class Services(FirestoreAPI):

    def __init__(self, application_id: str) -> None:
        self.application_id = application_id        
        super().__init__(collection=f"application/{self.application_id}/services")

    def add(self, data: ServiceModel):
        batch = self.fcli.batch()
        super().add_batch(batch, data.id , data)
        app = Application()
        app.add_batch_array(batch, self.application_id, 'services', data.dict())
        return batch.commit()    