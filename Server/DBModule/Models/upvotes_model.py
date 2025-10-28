from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Upvotes(Base):
    __tablename__ = "Upvotes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("User.id"))
    newsId = Column(Integer, ForeignKey("News.id"))

    user = relationship("User", back_populates="upvotes")
    news = relationship("News", back_populates="upvotes")