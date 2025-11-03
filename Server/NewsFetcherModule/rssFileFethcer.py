import os
import sys
import datetime
# If this file is run directly, ensure the repository root is on sys.path so
# imports like `from Server.DBModule.Models.news_model import News` work.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import logging
from inews_fetcher import INewsFetcher
import feedparser
from Server.DBModule.Models.news_model import News

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class RssFileFetcher(INewsFetcher):

    def __init__(self, rss_url: list[str]) -> None:
        self.rss_url = rss_url

    def fetch_news(self, url: str) -> None:
        feed = feedparser.parse(url)
        counter = 0
        for entry in feed.entries:
            counter += 1
            if counter > 7:
                break  # Limit to 20 entries per fetch
            if not hasattr(entry, 'published_parsed'):
                continue  # Skip entries without a publication date
            published = datetime.datetime(*entry.published_parsed[:6])
            news_items = []
            if published < datetime.datetime.now() - datetime.timedelta(hours=10):
                continue  # Skip news older than 10 minutes

            if not hasattr(entry, 'summary'):
                entry.summary = ""
                print(f"Entry missing summary: {entry}")
            if not hasattr(entry, 'title'):
                entry.title = "No Title"
            if not hasattr(entry, 'link'):
                entry.link = ""


            logger.debug(f"Title: {entry.title}")
            logger.debug(f"Published: {published}")
            logger.debug(f"Link: {entry.link}")
            logger.debug(f"Summary: {entry.summary}")
            logger.debug("-----\n\n")


            # TODO: Create News instance properly
            """ news_item = News()

            news_item.title=entry.title,
            news_item.description=entry.summary,
            news_item.link=entry.link,
            news_item.publicationDate=published,
            news_item.categoryId=1  # Default category ID 

            

            news_items.append(news_item)

        print(f"Fetched {len(news_items)} news items from {url}")"""
        

        # Save news_items to the database
        #self.save_news_items(news_items)

    def save_news_items(self, news_items: list[News]) -> None:
        # Implementation for saving news_items to the database
        # TODO: May be implemented somewhere else
        pass

    def testFetcher(self) -> None:
        """No-op implementation to satisfy INewsFetcher abstract method.

        This allows instantiating RssFileFetcher when running the module
        directly for testing.
        """
        return None

    def fetch_all_news(self) -> None:
        for url in self.rss_url:
            self.fetch_news(url)

if __name__ == "__main__":
    rss_urls = [
        "https://servis.idnes.cz/rss.aspx?c=zpravodaj",
    ]
    fetcher = RssFileFetcher(rss_urls)
    fetcher.fetch_all_news()
