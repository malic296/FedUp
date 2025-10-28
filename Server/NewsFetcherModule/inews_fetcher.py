from abc import ABC, abstractmethod

class INewsFetcher(ABC):
    @abstractmethod
    def testFetcher(self) -> None:
        pass