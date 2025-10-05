from pydantic import BaseModel
from typing import Optional

class Breed(BaseModel):
    name: str
    image: str
    description: str

class BreedList(Breed):
    id: int

    class Config:
        orm_mode = True