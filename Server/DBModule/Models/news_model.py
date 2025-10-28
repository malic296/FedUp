from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from . import Base

class News(Base):
    __tablename__ = "News"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)
    publicationDate = Column(DateTime)
    aiGeneratedText = Column(String, index=True)
    Embedding = Column(Vector(1500), index=True)
    validationText = Column(String, nullable=True, index=True)
    categoryId = Column(Integer, ForeignKey("Category.id"))

    category = relationship("Category", back_populates="news")
    upvotes = relationship("Upvotes", back_populates="news")