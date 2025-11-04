from abc import ABC, abstractmethod
from typing import List

class IAIService(ABC):
    @abstractmethod
    def generateNewsDependencies(self, news: List[str]):
        pass
