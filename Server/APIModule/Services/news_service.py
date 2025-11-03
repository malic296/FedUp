import os
from dotenv import load_dotenv

from Server.NewsFetcherModule.news_fetcher import NewsFetcher
from ..Interfaces.inews_service import INewsService

class NewsService(INewsService):
    def __init__(self):
        self.news_fetcher = NewsFetcher()

    def testNews(self):
        return "test"

    def fetch_news_from_API(self, limit: int = 1):
        """Fetch latest articles via NewsFetcher."""
        return self.news_fetcher.fetch_news_from_API(limit=limit)