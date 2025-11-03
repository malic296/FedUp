import os

from dotenv import load_dotenv
import requests
import traceback
from .inews_fetcher import INewsFetcher

class NewsFetcher(INewsFetcher):
    """
    Concrete implementation of INewsFetcher that fetches latest news
    from TheNewsAPI (/v1/news/top) and returns minimal info for each article.
    """

    def fetch_news_from_API(self, limit: int = 1):
        """
        Fetch latest articles from TheNewsAPI /v1/news/top.

        Reads `THENEWSAPI_KEY` from Server/server.env or environment.
        Returns a list of articles with minimal fields: title, description, link, publicationDate.
        """

        # Load environment variables from server.env
        env_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..", "..", "server.env")
        )
        if os.path.exists(env_path):
            load_dotenv(env_path)

        api_key = os.getenv("THENEWSAPI_KEY") or os.getenv("NEWSAPI_KEY")
        if not api_key:
            return {"error": "THENEWSAPI_KEY not set"}

        # TheNewsAPI endpoint and query parameters
        url = "https://api.thenewsapi.com/v1/news/top"
        params = {"api_token": api_key, "limit": limit}

        # Make the HTTP request and handle errors
        try:
            resp = requests.get(url, params=params, timeout=15)
            resp.raise_for_status()
            payload = resp.json()
        except requests.RequestException as e:
            return {"error": f"HTTP error: {e}", "trace": traceback.format_exc()}
        except ValueError as e:
            return {"error": f"JSON decode error: {e}", "trace": traceback.format_exc()}

        # Extract articles from response
        items = payload.get("data") or payload.get("articles") or []
        if not items:
            return {"error": "No articles returned", "raw": payload}

        # Map only minimal information
        result = []
        for a in items:
            result.append({
                "title": a.get("title") or a.get("headline") or "",
                "description": a.get("description") or a.get("excerpt") or "",
                "link": a.get("url") or a.get("link") or "",
                "publicationDate": a.get("published_at")
            })
        return result
