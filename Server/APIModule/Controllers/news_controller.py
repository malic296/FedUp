from fastapi import APIRouter, Depends
from ..Services.news_service import NewsService

router = APIRouter()
news_service = NewsService()

@router.get("/")
def testNews():
    return news_service.testNews()
