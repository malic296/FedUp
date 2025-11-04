from abc import ABC, abstractmethod

class INewsFetcher(ABC):
    @abstractmethod
    def fetch_news_rss(self) -> None:
        pass