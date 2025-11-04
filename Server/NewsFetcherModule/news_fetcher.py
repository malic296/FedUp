import datetime
from .inews_fetcher import INewsFetcher
import feedparser
import logging

class NewsFetcher(INewsFetcher):
    def fetch_news_rss(self) -> None:
        url_list = ["https://servis.idnes.cz/rss.aspx?c=zpravodaj","https://www.denik.cz/rss/zpravy.html"]
        for url in url_list:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                if not hasattr(entry, 'published_parsed'):
                    continue  
                published = datetime.datetime(*entry.published_parsed[:6])
                news_items = []
                if published < datetime.datetime.now() - datetime.timedelta(minutes=1000):
                    continue  

                if not hasattr(entry, 'summary'):
                    entry.summary = ""
                    print(f"Entry missing summary: {entry}")
                if not hasattr(entry, 'title'):
                    entry.title = "No Title"
                if not hasattr(entry, 'link'):
                    entry.link = ""

                result = []
                result.append({
                    "title": {entry.title},
                    "description": {entry.description},
                    "link": {entry.link},
                    "publicationDate": {published},
                    "author": {entry.get("credit")},
                    "language": ""
                })

                for x in result:
                    print(x["author"])

                
