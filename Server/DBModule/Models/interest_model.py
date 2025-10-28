from sqlalchemy import Column, Integer, ForeignKey
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import relationship
from . import Base

class Interest(Base):
    __tablename__ = "Interest"

    id = Column(Integer, primary_key=True, autoincrement=True)
    interestEmbedding = Column(Vector(1500), index=True)

    users = relationship("User_Interest", back_populates="interest")