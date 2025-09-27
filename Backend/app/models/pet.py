from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..database import Base


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    breed_id = Column(Integer, ForeignKey("breed.id"))
    owner_id = Column(Integer, ForeignKey("user.id"))
    gender = Column(String(2), nullable=False)
    birth_date = Column(Date, nullable=False)
    vaccine = Column(String(200), nullable=True)
    img = Column(String(200), nullable=True)

    owner = relationship("User", back_populates="pets")
    breed = relationship("Breed")