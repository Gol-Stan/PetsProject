from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas
from app.models import Breed

""" Breed creation """
async def create_breed(db: AsyncSession, breed_in: schemas.breed.Breed):
    existing = await db.execute(select(models.Breed).where(models.Breed.name == breed_in.name))
    if existing.scalars().first():
        raise ValueError("Breed with this name already exists")

    new_breed = models.Breed(
        name=breed_in.name,
        image=breed_in.img,
        description=breed_in.description
    )
    db.add(new_breed)
    await db.commit()
    await db.refresh(new_breed)

    return new_breed

""" Update breed """
async def update_breed(db: AsyncSession, breed_id: int, breed_in: schemas.breed.Breed):
    result = await db.execute(select(models.Breed).where(models.Breed.id == breed_id))
    breed = result.scalars().first()

    if not breed:
        return None

    if breed_in.name is not None:
        breed.name = breed_in.name
    if breed_in.img is not None:
        breed.image = breed_in.img
    if breed_in.description is not None:
        breed.description = breed_in.description

    await db.commit()
    await db.refresh(breed)
    return breed

""" Get breed by id """
async def get_breed_by_id(db: AsyncSession, breed_id: int):
    result = await db.execute(select(models.Breed).where(models.Pet.breed_id == breed_id))
    return result.scalars().first()


""" Delete breed """
async def delete_breed(db: AsyncSession, breed_id: int):
    pets_result = await db.execute(select(models.Pet).where(models.Pet.breed_id == breed_id))
    if pets_result.scalars().first():
        raise ValueError("Cannot delete breed - there are pets associated with it")

    result = await db.execute(select(models.Breed).where(models.Breed.id == breed_id))
    breed = result.scalars().first()
    if not breed:
        return None

    await db.delete(breed)
    await db.commit()
    return breed

""" Show all breeds """
async def get_all_breeds(db: AsyncSession):
    result = await db.execute(select(Breed))
    return result.scalars().all()