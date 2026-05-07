from .base_service import BaseService
from web.api_client.api.themes import themes
from web.api_client.models import PagedThemesDTO
from ..api_client.client import AuthenticatedClient

class ThemesService(BaseService):
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def read_themes(self, hours: int, cursor: str | None, page: int | None) -> PagedThemesDTO:
        response = themes.sync_detailed(
            client=self.client,
            hours=hours,
            cursor=cursor,
            page=page
        )

        self._handle_response(response)

        return response.parsed