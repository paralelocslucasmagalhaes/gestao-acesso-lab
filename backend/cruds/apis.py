
from cruds.firestore import FirestoreAPI
from models.models import ApisModel
from cruds.scope import Scopes
from cruds.services import Services
from cruds.application import Application



class APIs(FirestoreAPI):

    def __init__(self, application_id: str, service_id: str, scope_id: str) -> None:
        self.application_id = application_id
        self.service_id = service_id
        self.scope_id = scope_id
        super().__init__(collection=f"application/{self.application_id}/services/{self.service_id}/scopes/{self.scope_id}/apis")

    def add(self, data: ApisModel):
        batch = self.fcli.batch()
        super().add_batch(batch, data.id, data)
        
        scopes = Scopes(self.application_id, self.service_id)
        scopes.add_batch_array(batch, self.scope_id, 'apis', data.dict())

        scope_doc = scopes.get(self.scope_id)
        doc_scopes = self.update_array(data.dict(), scope_doc, 'apis')
        scope_doc.update({'apis': doc_scopes})

        service = Services(self.application_id)
        service.add_batch_array(batch, self.service_id, 'scopes', scope_doc)

        service_doc = service.get(self.service_id)
        service_scope = self.update_array(scope_doc, service_doc , 'scopes')
        service_doc.update({'scopes': service_scope})

        app = Application()
        app.add_batch_array(batch, self.application_id, 'services', service_doc)
        return batch.commit()
    
   