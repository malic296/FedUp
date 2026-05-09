import uuid
from api.models import Channel, ScrapedChannel, ArticleSearchEntry, Article
from api.core.errors import DatabaseError, MappingError
from .base_repository import BaseRepository
from api.interfaces import ChannelInterface

class ChannelRepository(BaseRepository, ChannelInterface):
    def get_channels(self, user_id: int) -> list[Channel]:
        query = """
            SELECT id, uuid, title, link, logo_url,  
            EXISTS(
                SELECT 1 
                FROM disabled 
                WHERE consumer_id = %s AND channel_id = channel.id
            ) AS disabled_by_user
            FROM channel
        """
        params = (user_id, )
        db_result = self._execute(query=query, params=params)
        if not db_result.success:
            raise DatabaseError(
                message=db_result.error_message if db_result.error_message else "Unknown error",
                method="get_channels"
            )

        try:
            return [Channel(**channel) for channel in db_result.data]
        except Exception as e:
            raise MappingError(mapping_error=str(e), method="get_channels")

    def set_disabled_channels_by_uuids(self, user_id: int, disabled_uuids: list[str]) -> None:
        inserts = [("DELETE FROM disabled WHERE consumer_id = %s", (user_id,))]

        query = """
            INSERT INTO disabled (consumer_id, channel_id) 
            SELECT %s, id
            FROM channel
            WHERE uuid = ANY(%s)
        """

        inserts.append((query, (user_id, disabled_uuids, )))

        db_result = self._execute_transaction(inserts)
        if not db_result.success:
            raise DatabaseError(
                message=db_result.error_message if db_result.error_message else "Unknown error",
                method="set_disabled_channels_by_uuids"
            )

    def get_new_articles(self, channels: list[ScrapedChannel]) -> list[tuple[int, list[Article]]]:
        channel_insert = """
            INSERT INTO channel (uuid, title, link, logo_url) 
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (link) DO UPDATE SET title = EXCLUDED.title
            RETURNING id, link
        """
        channel_queries = []

        for channel in channels:
            channel_queries.append((channel_insert, (channel.uuid, channel.title, channel.link, channel.logo_url, )))

        ch_result = self._execute_transaction_returning(channel_queries)

        if not ch_result.success:
            raise DatabaseError(
                message=ch_result.error_message if ch_result.error_message else "Unknown error",
                method="update_channels"
            )

        channel_id_map = {row["link"]: row["id"] for row in ch_result.data}

        all_scraped_links = [art.link for ch in channels for art in ch.articles]
        check_sql = "SELECT link FROM article WHERE link = ANY(%s)"
        existing_res = self._execute(check_sql, (all_scraped_links,))
        existing_links = {row["link"] for row in existing_res.data} if existing_res.data else set()

        final_output = []
        for channel in channels:
            db_id = channel_id_map.get(channel.link)

            new_only = [
                art for art in channel.articles
                if art.link not in existing_links
            ]

            if new_only:
                final_output.append((db_id, new_only))

        return final_output

    def get_disabled_channel_ids_for_user(self, consumer_id: int) -> list[int]:
        query = "SELECT channel_id FROM disabled WHERE consumer_id = %s"
        params = (consumer_id,)
        db_result = self._execute(query=query, params=params)
        if not db_result.success:
            raise DatabaseError(
                message=db_result.error_message if db_result.error_message else "Unknown error",
                method="get_disabled_channel_ids_for_user"
            )
        return [row["channel_id"] for row in (db_result.data  if db_result.data else [])]