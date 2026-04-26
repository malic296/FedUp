from dataclasses import dataclass
from .article import Article

@dataclass
class PagedArticles:
    articles: list[Article]
    next_cursor: str | None = None
    has_more: bool = False