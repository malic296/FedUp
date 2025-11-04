from .iai_service import IAIService
from typing import List
from ..DBModule.Models import News

class AIService(IAIService):
    def generateNewsDependencies(self, news: List[str]):

        results = []

        for x in news:
            results.append(News(
                author=x["author"],
                title=x["title"],
                description=x["description"],
                link=x["link"],
                publicationDate=x["publicationDate"],
                language=x["language"]
                #categoryId=x["categoryId"]
            ))


        #TODO: Those operations will be done in english -> translate czech texts before creating embeddings and other AI products
        # Create AI Generated text

        # Create embeddings


        