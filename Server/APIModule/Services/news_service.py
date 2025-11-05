import os
from dotenv import load_dotenv

from Server.NewsFetcherModule.news_fetcher import NewsFetcher
from Server.APIModule.Interfaces.inews_service import INewsService

class NewsService(INewsService):
    def __init__(self):
        self.news_fetcher = NewsFetcher()

    def testNews(self):
        return "test"