import os
import time

from dotenv import load_dotenv, find_dotenv
import requests
from .inews_fetcher import INewsFetcher
from datetime import datetime, timedelta, timezone
from deep_translator import GoogleTranslator

class NewsFetcher(INewsFetcher):

    def fetch_news_from_API(self):
        load_dotenv(find_dotenv("server.env"))
        api_key = os.getenv("THENEWSAPI_KEY")
        url = os.getenv("API_URL")

        published_from = (datetime.now(timezone.utc) - timedelta(minutes=100)).strftime("%Y-%m-%dT%H:%M:%S")
        params = {"api_token": api_key, "language": "cs", "published_after": published_from, "limit" : 1}

        try:
            resp = requests.get(url, params=params, timeout=15)
            resp.raise_for_status()
            payload = resp.json()
        except Exception:
            return []

        items = payload.get("data")
        if not items:
            return []

        result = []
        for a in items:
            result.append({
                "author": a.get("source"),
                "title": a.get("title"),
                "description": a.get("description") or a.get("excerpt"),
                "link": a.get("url") or a.get("link"),
                "publicationDate": a.get("published_at"),
                "language": a.get("language"),
                "category": (a.get("categories") or "")[0]
            })

        for x in result:
            #TODO:
            #Save category to DB and get corresponding FK -> save that id value to "categoryId"

            print(x)
            

            
        return result
