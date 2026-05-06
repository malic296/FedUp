from datetime import datetime, timedelta, timezone
from api.core.errors import DatabaseError
from api.interfaces import ThemesInterface
from api.models import Theme, Article
from api.repositories.base_repository import BaseRepository

class ThemesRepository(ThemesInterface, BaseRepository):
    def read_themes(self, hours: int = 72) -> list[Theme]:
        since_date = datetime.now(timezone.utc) - timedelta(hours=hours)
        query = """
            SELECT t.id AS theme_id, t.uuid AS theme_uuid, t.newest_date AS theme_newest_date,
            a.id AS article_id, a.uuid as article_uuid, a.title as article_title, a.description as article_description, a.link as article_link, a.pub_date as article_pub_date, a.embedding AS article_embedding,
            c.link as channel_link, c.logo_url as channel_logo
            FROM theme AS t 
            JOIN article AS a ON a.theme_id = t.id
            JOIN channel AS c ON c.id = a.channel_id
            WHERE t.newest_date >= %s
            ORDER BY t.newest_date DESC
        """

        result = self._execute(query=query, params=(since_date, ))
        if not result.success:
            raise DatabaseError(
                message=result.error_message if result.error_message else "Unknown error",
                method="read_themes"
            )

        theme_map = {}

        for row in result.data:
            if row["theme_id"] not in theme_map:
                theme_map[row["theme_id"]] = Theme(id=row["theme_id"], uuid=row["theme_uuid"], newest_date=row["theme_newest_date"], articles = [])

            theme_map[row["theme_id"]].articles.append(
                Article(
                    id=row["article_id"],
                    uuid=row["article_uuid"],
                    title=row["article_title"],
                    description=row["article_description"],
                    link=row["article_link"],
                    pub_date=row["article_pub_date"],
                    embedding=row["article_embedding"],
                    channel_logo=row["channel_logo"],
                    channel_link=row["channel_link"],
                    likes=None
                )
            )

        return list(theme_map.values())

