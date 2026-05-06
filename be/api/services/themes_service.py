from api.interfaces.themes_interface import ThemesInterface
from api.models import Theme

class ThemesService:
    def __init__(self, themes_repository: ThemesInterface):
        self.themes = themes_repository

    def read_themes(self, hours: int = 72) -> list[Theme]:
        return self.themes.read_themes(hours)