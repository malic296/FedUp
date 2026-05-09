from dataclasses import dataclass, field
from .article import Article, ArticleWithChannelID

@dataclass
class ThemeCandidates:
    new_articles: list[ArticleWithChannelID] = field(default_factory=list)
    unthemed_articles: list[Article] = field(default_factory=list)