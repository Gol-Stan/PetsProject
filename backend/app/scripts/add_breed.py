import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import AsyncSessionLocal  # ваша сессия
from app import models, schemas
from app.crud import create_breed  # ваша функция

async def main():
    async with AsyncSessionLocal() as session:  # открываем асинхронную сессию
        breed_in = schemas.breed.BreedCreate(
            name="Yorkshire Terrier",
            img="/static/breeds/yorkshire_terrier.jpg",
            description= """Origin: United Kingdom
Type: Companion / Toy dog
Size: Small / Toy
Height: 15-23 cm
Weight: 2-3 kg
Lifespan: 12-15 years

Appearance:
Long, silky, fine coat — requires regular grooming
Small, compact body with erect ears
Dark eyes with alert expression
Coat colors: steel blue and tan

Pros:
Lively, playful, and affectionate — bonds well with owners
Small size — идеально для квартиры
Intelligent and trainable — enjoys mental stimulation
Alert — good watchdog despite size

Cons / Challenges:
High grooming needs — daily brushing recommended
Can be stubborn — requires consistent training
Prone to dental issues — regular care needed
Fragile due to small size — careful handling required

Ideal owners:
Individuals or families seeking a small, lively companion
Owners able to provide grooming, training, and socialization
Suitable for those wanting an intelligent and affectionate toy dog"""
        )
        breed = await create_breed(session, breed_in)
        print(f"Breed created: {breed.name}, id={breed.id}")

if __name__ == "__main__":
    asyncio.run(main())
