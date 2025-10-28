from abc import ABC, abstractmethod

class IDBService(ABC):
    @abstractmethod
    def getNewsValidation(self, newsId : int) -> str:
        pass