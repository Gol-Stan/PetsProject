from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated ="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user_in: schemas.User.UserCreate):
    hashed_pw = pwd_content.hash(user_in.password)
    db_user = models.User(
        name=user_in.name,
        email=user_in.email,
        phone=user_in.phone,
        hashed_password = hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_content.verify(plain_password, hashed_password)