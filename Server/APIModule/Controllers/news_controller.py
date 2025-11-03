from fastapi import APIRouter, Depends
from ..Services.news_service import NewsService

router = APIRouter()
news_service = NewsService()

@router.get("/")
def testNews():
    return news_service.testNews()

@router.get("/fetch")
def fetch_news_from_API(limit: int = 1):
    """
    Fetch the latest articles directly from TheNewsAPI.
    Optional query parameter `limit` (default 1) controls number of articles returned.
    """
    return news_service.fetch_news_from_API(limit=limit)