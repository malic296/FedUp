from abc import ABC, abstractmethod

class INewsFetcher(ABC):
    @abstractmethod
    def fetch_news_from_API(self, limit: int = 5):
        pass

    @abstractmethod
    def fetch_news(self):
        pass