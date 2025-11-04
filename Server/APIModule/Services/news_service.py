import os
from dotenv import load_dotenv

from NewsFetcherModule.news_fetcher import NewsFetcher
from ..Interfaces.inews_service import INewsService

class NewsService(INewsService):
    def __init__(self):
        self.news_fetcher = NewsFetcher()

    def testNews(self):
        return "test"