from dataclasses import asdict
from fastapi import APIRouter, Depends
from api.api.dependencies import get_themes_service
from api.models import Theme
from api.schemas.responses.theme_responses import ThemesResponse
from api.schemas.article_dto import ArticleDTO
from api.schemas.theme_dto import ThemeDTO
from api.api.dependencies import get_current_user

themes_router = APIRouter(
    prefix="/themes",
    tags=["themes"]
)

@themes_router.get("/", response_model=ThemesResponse)
def themes(hours: int, themes_service = Depends(get_themes_service), user = Depends(get_current_user)):
    themes_data: list[Theme] = themes_service.read_themes(hours=hours)

    mapped_themes = []
    for theme in themes_data:
        articles_dtos = [
            ArticleDTO(**asdict(art))
            for art in (theme.articles or [])
        ]

        theme_dto = ThemeDTO(
            uuid=theme.uuid,
            newest_date=theme.newest_date,
            articles=articles_dtos
        )
        mapped_themes.append(theme_dto)

    return ThemesResponse(
        success=True,
        message="Themes fetched correctly",
        themes=mapped_themes
    )