from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from APIModule.Controllers.users_controller import router as users_router
from APIModule.Controllers.news_controller import router as news_router
from NewsFetcherModule.scheduler import lifespan  

app = FastAPI(lifespan=lifespan)
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(news_router, prefix="/news", tags=["News"])

# "/" -> Swagger UI
@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/docs")
