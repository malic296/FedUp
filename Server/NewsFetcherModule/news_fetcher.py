import datetime
from .inews_fetcher import INewsFetcher

class NewsFetcher(INewsFetcher):
    def testFetcher(self):
        print(datetime.datetime.now()) 