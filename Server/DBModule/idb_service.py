from abc import ABC, abstractmethod
from .Models.category_model import Category
from .Models.news_model import News
from typing import List, Optional

class IDBService(ABC):
    @abstractmethod
    def get_all_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def get_category_id(self, category: str) -> Optional[int]:
        pass

    @abstractmethod
    def create_category(self, category : Category) -> int:
        pass

    @abstractmethod
    def save_news(self, news : List[News]) -> None:
        pass

    @abstractmethod
    def getNewsValidation(self, newsId : int) -> str:
        pass

    @abstractmethod
    def get_news(self) -> List[News]:
        pass