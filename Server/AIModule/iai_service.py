from abc import ABC, abstractmethod

class IAIService(ABC):
    @abstractmethod
    def generateAIDescription(self, text: str) -> str:
        pass
