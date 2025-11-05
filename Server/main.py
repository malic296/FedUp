from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .APIModule.Controllers.users_controller import router as users_router
from .APIModule.Controllers.news_controller import router as news_router
from Server.NewsFetcherModule.scheduler import lifespan
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI(lifespan=lifespan)
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(news_router, prefix="/news", tags=["News"])

origins = [
    "*",                    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # <- which origins are allowed
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],            # any custom headers
)

# "/" -> Swagger UI
@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/docs")
