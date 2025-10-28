from pydantic import BaseModel
from datetime import datetime

class NewsDTO(BaseModel):
    id : int
    link : str
    publicationDate : datetime
    generatedText : str
    category : str
    validationText: str