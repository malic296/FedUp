from api.interfaces import ElasticSearchInterface, ArticleInterface, ChannelInterface, ThemesInterface
from api.services import SemanticService
from api.models import ThemeCandidate

class UpdateService:
    def __init__(self, scraping_service, themes: ThemesInterface, articles: ArticleInterface, channels: ChannelInterface, elasticsearch: ElasticSearchInterface, semantics: SemanticService):
        self.scraping_service = scraping_service
        self.themes = themes
        self.articles = articles
        self.channels = channels
        self.elasticsearch = elasticsearch
        self.semantics = semantics

    async def update_data(self, channel_urls: list[str], hours: int) -> None:
        channels = await self.scraping_service.fetch_channels(feeds=channel_urls, hours=hours)
        new_data = self.channels.get_new_articles(channels)

        candidates: list[ThemeCandidate] = []
        themes = self.themes.get_all_themes(hours=hours)
        for channel_id, articles in new_data:
            for article in articles:
                if article.embedding is None:
                    normalized_text = self.semantics.normalize_text(article.title + " " + article.description)
                    article.embedding = self.semantics.create_embedding(normalized_text)

                theme_id = None
                for theme in themes:
                    for themed_article in theme.articles:
                        if self.semantics.get_similarity_percentage(themed_article.embedding, article.embedding) > 75:
                            theme_id = theme.id
                            break

                    if theme_id:
                        break

                candidates.append(
                    ThemeCandidate(
                        channel_id=channel_id,
                        new_article=article,
                        unthemed_articles = [],
                        existing_theme_id=theme_id
                    )
                )

        unthemed_articles = self.articles.get_unthemed_articles(hours=hours)

        for candidate in candidates:
            for unthemed_article in unthemed_articles:
                if self.semantics.get_similarity_percentage(candidate.new_article.embedding, unthemed_article.embedding) > 75:
                    candidate.unthemed_articles.append(unthemed_article)
                    unthemed_articles.remove(unthemed_article)

            for theme in themes:
                for article in theme.articles:
                    if self.semantics.get_similarity_percentage(candidate.new_article.embedding, article.embedding) > 75:
                        candidate.existing_theme_id = theme.id
                        break

                if candidate.existing_theme_id:
                    break







        self.elasticsearch.save_article_entries(es_entries_to_save)

        self.articles.assign_new_themes(hours_limit=72)




