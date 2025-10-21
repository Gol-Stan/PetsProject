from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


class OwnerPublic(BaseModel):
    name: str
    phone: Optional[str] = None

    class Config:
        from_attributes = True


class OwnerPrivate(BaseModel):
    name: str
    phone: Optional[str] = None
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: Optional[str] = None
    exp: Optional[int] = None