from dataclasses import dataclass
from .article import Article

@dataclass
class ThemeCandidate:
    channel_id: int
    new_article: Article
    unthemed_articles: list[Article]
    existing_theme_id: int | None = None # If article does match existing theme it will only get added via this id