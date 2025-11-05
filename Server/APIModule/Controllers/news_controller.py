from fastapi import APIRouter, Depends
from Server.APIModule.Services.news_service import NewsService

router = APIRouter()
news_service = NewsService()

@router.get("/")
def testNews():
    return news_service.testNews()
