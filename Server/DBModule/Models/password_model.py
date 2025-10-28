from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Password(Base):
    __tablename__ = "Password"

    id = Column(Integer, primary_key=True, autoincrement=True)
    salt = Column(String)
    hash = Column(String)

    user = relationship("User", back_populates="password", uselist=False)