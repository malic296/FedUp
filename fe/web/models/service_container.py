from dataclasses import dataclass
from web.services import ArticlesService, ChannelsService, ConsumersService

@dataclass
class ServiceContainer:
    articles: ArticlesService
    channels: ChannelsService
    consumers: ConsumersService
