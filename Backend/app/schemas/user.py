from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


class OwnerPublic(BaseModel):
    name: str
    phone: Optional[str] = None

    class Config:
        orm_mode = True


class OwnerPrivate(BaseModel):
    name: str
    phone: Optional[str] = None
    email: EmailStr

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: Optional[str] = None
