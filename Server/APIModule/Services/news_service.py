from ..Interfaces.inews_service import INewsService

class NewsService(INewsService):
    def testNews(self):
        return "test"