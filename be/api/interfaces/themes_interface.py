from abc import ABC, abstractmethod
from api.models import Theme, ArticleWithChannelID, ArticleSearchEntry, ThemeCandidates

class ThemesInterface(ABC):
    @abstractmethod
    def read_themes(self, consumer_id: int, sort_value: str | None, uuid: str | None, hours: int = 72)  -> list[Theme]:
        ...

    @abstractmethod
    def get_all_themes_without_articles(self, hours: int) -> list[Theme]:
        ...

    @abstractmethod
    def add_articles_to_existing_themes(self, new_themed_articles: list[ArticleWithChannelID]) -> list[ArticleSearchEntry]:
        ...

    @abstractmethod
    def save_candidates_to_new_themes(self, candidates: list[ThemeCandidates]) -> list[ArticleSearchEntry]:
        ...