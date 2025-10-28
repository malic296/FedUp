from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from . import Base

class Category(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    categoryEmbedding = Column(Vector(1500), index=True)

    news = relationship("News", back_populates="category")
    users = relationship("User_Category", back_populates="category")