from pydantic import BaseModel
from typing import Optional
from datetime import date

class PetBase(BaseModel):
    name: str
    gender: str
    birth_date: date
    breed: str
    vaccine: Optional[str]
    qr: str

class PetList(PetBase):
    id: int

    class Config:
        orm_mode = True

class OwnerDetail(BaseModel):
    name: str
    phone: str

    class Config:
        orm_mode = True

class PetDetail(PetBase):
    id: int
    owner: OwnerDetail

    class Config:
        orm_mode = True
