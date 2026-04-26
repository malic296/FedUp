from .base_response import BaseResponse
from api.schemas import ChannelDTO

class ChannelsResponse(BaseResponse):
    channels: list[ChannelDTO]