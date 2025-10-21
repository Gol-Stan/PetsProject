from pydantic import BaseModel
from typing import Optional
from datetime import date

from app.schemas.user import OwnerPublic, OwnerPrivate


class PetBase(BaseModel):
    name: str
    gender: str
    birth_date: date
    breed_id: int
    vaccine: Optional[str] = None
    img: Optional[str] = None

class PetCreate(BaseModel):
    pass

class PetUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    breed_id: Optional[int] = None
    vaccine: Optional[str] = None
    img: Optional[str] = None

class PetList(PetBase):
    id: int
    qr_code: str

    class Config:
        from_attributes = True

class PetPublic(PetBase):
    id: int
    owner: OwnerPublic

    class Config:
        from_attributes = True

class PetPrivate(PetBase):
    id: int
    owner: OwnerPrivate

    class Config:
        from_attributes = True
