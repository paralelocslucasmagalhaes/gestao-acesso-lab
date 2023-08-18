
from models.models import ScopeModel
from cruds.firestore import FirestoreAPI
from cruds.application import Application
from cruds.services import Services


class Scopes(FirestoreAPI):

    def __init__(self, application_id: str, service_id: str) -> None:
        self.application_id = application_id
        self.service_id = service_id        
        super().__init__(collection=f"application/{self.application_id}/services/{self.service_id}/scopes")

    def add(self, data: ScopeModel):
        batch = self.fcli.batch()
        super().add_batch(batch, data.id, data)
        service = Services(self.application_id)
        service.add_batch_array(batch, self.service_id, 'scopes', data.dict())
        doc_service = service.get(self.service_id)

        service_scope = self.update_array(data.dict(), service.get(self.service_id), 'scopes')
        doc_service.update({'scopes': service_scope})
        
        app = Application()
        app.add_batch_array(batch, self.application_id, 'services', doc_service)
        return batch.commit()
    