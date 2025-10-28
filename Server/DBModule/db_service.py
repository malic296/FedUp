from .idb_service import IDBService

class DBService(IDBService):
    def getNewsValidation(self, newsId : int):
        return str(newsId)