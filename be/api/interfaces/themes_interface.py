from abc import ABC, abstractmethod
from api.models import Theme

class ThemesInterface(ABC):
    @abstractmethod
    def read_themes(self, hours: int = 72) -> list[Theme]:
        ...