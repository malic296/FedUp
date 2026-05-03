from contextlib import asynccontextmanager
from fastapi import FastAPI
from ml.core.logger import setup_logging
from ml.core.utils import load_model
from ml.models import ServiceContainer
from ml.services import EmbeddingsService, NormalizationService

setup_logging()
model = load_model()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # SERVICES
    embeddings_service = EmbeddingsService(model = model)
    normalization_service = NormalizationService()

    app.state.services = ServiceContainer(
        embeddings=embeddings_service,
        normalization=normalization_service
    )

    yield