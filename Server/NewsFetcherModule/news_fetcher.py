import os
import time

from dotenv import load_dotenv, find_dotenv
import requests
from pathlib import Path
from .inews_fetcher import INewsFetcher
from datetime import datetime, timedelta, timezone
from deep_translator import GoogleTranslator
from Server.AIModule.ai_service import AIService
from Server.DBModule.db_service import DBService

class NewsFetcher(INewsFetcher):
    def __init__(self):
        this_dir = Path(__file__).resolve().parent 
        env_path = this_dir.parent / "server.env" 

        load_dotenv(dotenv_path=env_path, override=True)
        load_dotenv(find_dotenv("server.env"))
        self.ai_service = AIService()
        self.db_service = DBService()

    def fetch_news_from_API(self):
        api_key = os.getenv("THENEWSAPI_KEY")
        url = os.getenv("API_URL")

        published_from = (datetime.now(timezone.utc) - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")
        params = {"api_token": api_key, "language": "en,cs", "published_after": published_from}

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
                "description": a.get("description"),
                "link": a.get("url") or a.get("link"),
                "publicationDate": a.get("published_at"),
                "language": a.get("language"),
                "category": a.get("categories")[0] if a.get("categories") else ""
            })
         
        self.ai_service.generateNewsDependencies(result)

    def fetch_news(self):
        all_news = self.db_service.get_news()
        for news in all_news:
            print(f"Title: {news.title}, Upvotes: {news.upvotes_count}")
        return all_news