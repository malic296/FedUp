from abc import ABC, abstractmethod

class INewsService(ABC):
    @abstractmethod
    def testNews(self) -> str:
        pass