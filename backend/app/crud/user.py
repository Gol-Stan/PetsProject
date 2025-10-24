from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated ="auto")

MAX_BCRYPT_LEN = 72

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_in: schemas.user.UserCreate):
    existing = await get_user_by_email(db, user_in.email)
    if existing:
        raise ValueError("User already exists")

    password_to_hash = user_in.password[:MAX_BCRYPT_LEN]
    hashed_pw = pwd_context.hash(password_to_hash)
    db_user = models.User(
        name=user_in.name,
        email=user_in.email,
        phone=user_in.phone,
        hashed_password=hashed_pw,
        is_admin=user_in.is_admin
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, user_id: int, user_update: schemas.user.UserUpdate):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        return None

    update_data = user_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        if field == "password" and value:
            pass_to_hash = value[:MAX_BCRYPT_LEN]
            user.hashed_password = pwd_context.hash(pass_to_hash)
        elif hasattr(user, field) and value is not None:
            setattr(user, field, value)

    await db.commit()
    await db.refresh(user)
    return user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def auth_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
