from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class User_Category(Base):
    __tablename__ = "User_Category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("User.id"))
    categoryId = Column(Integer, ForeignKey("Category.id"))

    user = relationship("User", back_populates="category")
    category = relationship("Category", back_populates="users")