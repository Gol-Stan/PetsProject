from pydantic import BaseModel
from typing import Optional
from datetime import date

from app.schemas.user import OwnerPublic, OwnerPrivate


class PetBase(BaseModel):
    name: str
    gender: str
    birth_date: date
    breed_id: int
    vaccine: Optional[str]
    img: str
    qr_code: str

class PetList(PetBase):
    id: int

    class Config:
        orm_mode = True

class PetPublic(PetBase):
    id: int
    owner: OwnerPublic

    class Config:
        orm_mode = True

class PetPrivate(PetBase):
    id: int
    owner: OwnerPrivate

    class Config:
        orm_mode = True
