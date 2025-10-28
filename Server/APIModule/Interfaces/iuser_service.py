from abc import ABC, abstractmethod

class IUserService(ABC):
    @abstractmethod
    def getUsername(self) -> str:
        pass