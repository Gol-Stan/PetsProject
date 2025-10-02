from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app import models, schemas
from app.services import qr

""" Create Pet """
async def create_pet(db: AsyncSession, pet_in: schemas.pet.PetBase, owner_id: int):

    qr_code = qr.generate_code()
    new_pet = models.Pet(
        name=pet_in.name,
        gender=pet_in.gender,
        birth_date=pet_in.birth_date,
        breed_id=pet_in.breed_id,
        vaccine=pet_in.vaccine,
        owner_id=owner_id,
        qr_code=qr_code
    )
    db.add(new_pet)
    await db.commit()
    await db.refresh(new_pet)

    qr.save_qr_image(qr_code)

    return new_pet

""" Search by qr-code """
async def get_pet_by_qr(db: AsyncSession, qr_code: str):
    result = await db.execute(select(models.Pet).where(models.Pet.qr_code == qr_code))
    return result.scalars().first()

""" Get all pets by owner """
async def get_my_pets(db:AsyncSession, owner_id: int):
    result = await db.execute(select(models.Pet).where(models.Pet.owner_id == owner_id))
    return result.scalars().all()

""" Update pet info """
async def update_pet(db: AsyncSession, pet_id: int, pet_in: schemas.pet.PetBase, owner_id: int):
    result = await db.execute(select(models.Pet).where(models.Pet.id == pet_id))
    pet = result.scalars().first()
    if not pet or pet.owner_id != owner_id:
        return None

    for key, value in pet_in.dict().items():
        setattr(pet, key, value)

    await db.commit()
    await db.refresh(pet)
    return pet

""" Delete pet from db """
async def delete_pet(db: AsyncSession, pet_id: int, owner_id: int):
    result = await db.execute(select(models.Pet).where(models.Pet.id == pet_id))
    pet = result.scalars().first()
    if not pet or pet.owner_id != owner_id:
        return None

    await db.delete(pet)
    await db.commit()
    return pet