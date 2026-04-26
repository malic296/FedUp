from .base_response import BaseResponse
from api.schemas import ConsumerDTO

class ConsumerResponse(BaseResponse):
    consumer: ConsumerDTO

class LikeResponse(BaseResponse):
    liked: bool