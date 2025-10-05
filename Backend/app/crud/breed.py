from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas


""" Breed creation """
async def create_breed(db: AsyncSession, breed_in: schemas.breed.Breed):
    new_breed = models.Breed(
        name=breed_in.name,
        image=breed_in.image,
        description=breed_in.description
    )
    db.add(new_breed)
    await db.commit()
    await db.refresh(new_breed)

    return new_breed

""" Update breed """
async def update_bread(db: AsyncSession, breed_id: int, breed_in: schemas.breed.Breed):
    result = await db.execute(select(models.Breed).where(models.Breed.id == breed_id))
    breed = result.scalars().first()

    if not breed:
        return None

    for key, value in breed_in.dict().items():
        setattr(breed, key, value)

    await db.commit()
    await db.refresh(breed)
    return breed

""" Delete breed """
async def delete_breed(db: AsyncSession, breed_id: int):
    result = await db.execute(select(models.Pet).where(models.Breed.id == breed_id))
    breed = result.scalars().first()
    if not breed:
        return None

    await db.delete(breed)
    await db.commit()
    return breed