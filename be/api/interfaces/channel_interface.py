from abc import ABC, abstractmethod
from api.models import Channel, ArticleSearchEntry, Article
from api.models.scraped_data import ScrapedChannel

class ChannelInterface(ABC):
    @abstractmethod
    def get_channels(self, user_id: int) -> list[Channel]:
        ...

    @abstractmethod
    def set_disabled_channels_by_uuids(self, user_id: int, channel_ids: list[str]) -> None:
        ...

    @abstractmethod
    def get_new_articles(self, channels: list[ScrapedChannel]) -> list[tuple[int, list[Article]]]:
        ...

    @abstractmethod
    def get_disabled_channel_ids_for_user(self, consumer_id: int) -> list[int]:
        ...