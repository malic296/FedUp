from api.models import Consumer, Article
from api.interfaces import ArticleInterface
from api.core.errors import ArticleNotFoundError
from api.core.cursor import decode_cursor
from .cache_service import CacheService
from api.models import PagedArticles

class ArticleService:
    def __init__(self, articles: ArticleInterface, cache: CacheService):
        self.articles = articles
        self.cache = cache

    def get_articles(self, consumer: Consumer, hours: int, order_by_likes: bool, cursor: str | None) -> PagedArticles:
        if hours > 72 or hours < 1:
            raise Exception("Hours must be <= 1 and 72 <=")

        sort_value, uuid = decode_cursor(cursor) if cursor else (None, None)

        return self.articles.get_articles(
            consumer=consumer,
            hours=hours,
            order_by_likes=order_by_likes,
            sort_value=sort_value,
            uuid=uuid
        )

    def get_article(self, uuid: str) -> Article:
        article = self.cache.get_article(uuid=uuid)
        if not article:
            article = self.articles.get_article(uuid=uuid)
            if article:
                self.cache.set_article(article=article)

        if not article:
            raise ArticleNotFoundError()

        return article

    def like_article(self, article_uuid: str, consumer: Consumer) -> bool:
        article_id = self.articles.article_uuid_to_id(article_uuid)
        if not article_id:
            raise ArticleNotFoundError()

        return self.articles.like_article(article_id=article_id, consumer_id=consumer.id)