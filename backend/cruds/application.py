
from cruds.firestore import FirestoreAPI

class Application(FirestoreAPI):

    def __init__(self) -> None:
        super().__init__(collection="application")