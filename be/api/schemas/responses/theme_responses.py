from .base_response import BaseResponse
from api.schemas.theme_dto import ThemeDTO

class ThemesResponse(BaseResponse):
    themes: list[ThemeDTO]