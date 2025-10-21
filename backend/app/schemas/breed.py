from pydantic import BaseModel
from typing import Optional

class Breed(BaseModel):
    name: str
    img: str
    description: str

class BreedCreate(Breed):
    pass

class BreedUpdate(BaseModel):
    name: Optional[str] = None
    img: Optional[str] = None
    description: Optional[str] = None

class BreedList(Breed):
    id: int

    class Config:
        from_attributes = True