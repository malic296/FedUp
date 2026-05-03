from dataclasses import dataclass
from ml.services import EmbeddingsService, NormalizationService

@dataclass
class ServiceContainer:
    embeddings: EmbeddingsService
    normalization: NormalizationService