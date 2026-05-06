from dataclasses import dataclass
from api.services import ArticleService, ChannelService, ConsumerService, EmailService, SecurityService, ThemesService

@dataclass(frozen=True)
class ServiceContainer:
    article_service: ArticleService
    channel_service: ChannelService
    consumer_service: ConsumerService
    email_service: EmailService
    security_service: SecurityService
    themes_service: ThemesService