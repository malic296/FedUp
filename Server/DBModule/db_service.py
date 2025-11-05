from .idb_service import IDBService
from contextlib import contextmanager
from .database import SessionLocal
from .Models.category_model import Category
from .Models.news_model import News
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

class DBService(IDBService):
    @staticmethod
    @contextmanager
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_all_categories(self) -> List[Category]:
        with self.get_db() as db:
            categories = db.query(Category).all()
            return categories
        
    def get_category_id(self, category: str) -> Optional[int]:
        with self.get_db() as db:
            query = select(Category.id).where(Category.category == category)
            return db.execute(query).scalar_one_or_none()

            
    def create_category(self, category : Category) -> int:
        with self.get_db() as db:
            query = select(Category.id).where(Category.category == category.category)
            db.add(category)
            try:
                db.commit()
                db.refresh(category)
                return category.id
            except IntegrityError:
                db.rollback()
                result = db.execute(query).scalar_one()
                return result
            
    def save_news(self, news : List[News]) -> None:
        with self.get_db() as db:
            for item in news:
                db.add(item)
            
            try:
                db.commit()

            except Exception as ex:
                print("Failed")

    def getNewsValidation(self, newsId : int):
        return str(newsId)