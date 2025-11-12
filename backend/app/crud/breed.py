from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from watchfiles import awatch

from app import models, schemas
from app.models import Breed
from app.services.breed_cache import breed_cache

""" Breed creation """
async def create_breed(db: AsyncSession, breed_in: schemas.breed.BreedCreate):
    existing = await db.execute(select(models.Breed).where(models.Breed.name == breed_in.name))
    if existing.scalars().first():
        raise ValueError("Breed with this name already exists")

    new_breed = models.Breed(
        name=breed_in.name,
        img=breed_in.img,
        description=breed_in.description
    )
    db.add(new_breed)
    await db.commit()
    await db.refresh(new_breed)

    await breed_cache.invalidate_all_breeds()

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
        breed.img = breed_in.img
    if breed_in.description is not None:
        breed.description = breed_in.description

    await db.commit()
    await db.refresh(breed)

    await breed_cache.invalidate_breed(breed_id)
    await breed_cache.invalidate_all_breeds()

    return breed

""" Get breed by id """
async def get_breed_by_id(db: AsyncSession, breed_id: int):
    cached_breeds = await breed_cache.get_breed_by_id()
    if cached_breeds:
        return cached_breeds

    result = await db.execute(select(models.Breed).where(models.Breed.id == breed_id))
    breed =  result.scalar_one_or_none()

    if breed:
        breeds_data = {
                "id": breed.id,
                "name": breed.name,
                "description": breed.description,
                "img": breed.img
                }
        await breed_cache.set_breed(breed_id, breeds_data)
        return breeds_data

    return None


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

    await breed_cache.invalidate_breed(breed_id)
    await breed_cache.invalidate_all_breeds()

    return breed

""" Show all breeds """
async def get_all_breeds(db: AsyncSession):
    cached_breeds = await breed_cache.get_all_breeds()
    if cached_breeds:
        return cached_breeds

    result = await db.execute(select(Breed))
    return result.scalars().all()

    breeds_data = [
        {
            "id": breed.id,
            "name": breed.name,
            "description": breed.description,
            "img": breed.img
        }
        for breed in breeds
    ]

    await breed_cache.set_all_breeds(breeds_data)
    return breeds_data

