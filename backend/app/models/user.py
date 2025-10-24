from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), nullable=True)
    hashed_password = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)

    pets = relationship("Pet", back_populates="owner")