from web.models import ServiceContainer
from web.services import ArticlesService, ChannelsService, ConsumersService
from flask import request, current_app
from web.api_client.client import AuthenticatedClient, Client

def get_services() -> ServiceContainer:
    token= request.cookies.get("access_token")
    base_url = current_app.config["API_URL"]

    if token:
        client = AuthenticatedClient(
            base_url=base_url,
            token=token,
            prefix="Bearer"
        )
    else:
        client = Client(
            base_url=base_url,
        )

    services = ServiceContainer(
        articles=ArticlesService(client),
        channels=ChannelsService(client),
        consumers=ConsumersService(client)
    )

    return services