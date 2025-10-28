from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class User_Interest(Base):
    __tablename__ = "User_Interest"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("User.id"))
    interestId = Column(Integer, ForeignKey("Interest.id"))

    user = relationship("User", back_populates="interests")
    interest = relationship("Interest", back_populates="users")