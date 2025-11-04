import os

from dotenv import load_dotenv, find_dotenv
import requests
from .inews_fetcher import INewsFetcher
from datetime import datetime, timedelta, timezone

class NewsFetcher(INewsFetcher):

    def fetch_news_from_API(self):
        # Load environment variables from server.env
        load_dotenv(find_dotenv("server.env"))
        api_key = os.getenv("THENEWSAPI_KEY")
        url = os.getenv("API_URL")

        published_from = (datetime.now(timezone.utc) - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")
        params = {"api_token": api_key, "language": "en,cs", "published_after": published_from, "limit" : 1}

        # Make the HTTP request and handle errors
        try:
            resp = requests.get(url, params=params, timeout=15)
            resp.raise_for_status()
            payload = resp.json()
        except Exception:
            return []

        # Extract articles from response
        items = payload.get("data") or payload.get("articles") or []
        if not items:
            return []

        # Map only minimal information
        result = []
        for a in items:
            result.append({
                "author": a.get("source"),
                "title": a.get("title"),
                "description": a.get("description") or a.get("excerpt"),
                "link": a.get("url") or a.get("link"),
                "publicationDate": a.get("published_at"),
                "language": a.get("language")
            })

        for x in result:
            print(x)

        return result
