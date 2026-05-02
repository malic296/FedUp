from dataclasses import dataclass
from datetime import datetime
from .article import Article

@dataclass
class Theme:
    uuid: str
    newest_date: datetime
    articles: list[Article] | None = None
    id: int | None = None