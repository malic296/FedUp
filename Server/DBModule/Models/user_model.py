from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    passwordId = Column(Integer, ForeignKey("Password.id"), unique=True)

    password = relationship("Password", back_populates="user")
    upvotes = relationship("Upvotes", back_populates="user")
    interests = relationship("User_Interest", back_populates="user")
    categories = relationship("User_Category", back_populates="user")