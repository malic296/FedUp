from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from .news_fetcher import NewsFetcher
from datetime import datetime

scheduler = BackgroundScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    fetcher = NewsFetcher()
    scheduler.add_job(fetcher.fetch_news_rss, "interval", minutes=10)
    scheduler.start()
    print(datetime.now())
    fetcher.fetch_news_rss()
    
    yield  

    scheduler.shutdown()
    print("Scheduler stopped")


app = FastAPI(lifespan=lifespan)
