from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base


class Breed(Base):
    __tablename__ = "breed"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    img = Column(String(500), nullable=False)
    description = Column(String(500), nullable=False)

