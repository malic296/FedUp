from fastapi import Depends, Request
from ml.models import ServiceContainer
from typing import Annotated

def get_services(request: Request) -> ServiceContainer:
    return request.app.state.services

def get_embeddings_service(services: Annotated[ServiceContainer, Depends(get_services)]):
    return services.embeddings

def get_normalization_service(services: Annotated[ServiceContainer, Depends(get_services)]):
    return services.normalization