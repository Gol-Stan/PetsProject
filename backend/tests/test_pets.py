import pytest


@pytest.mark.asyncio
async def test_pet_create(async_client):
    user_data = {
        "name": "Test User",
        "email": "pet@example.com",
        "password": "54545"
    }
    await async_client.post("/auth/register", json=user_data)

    login_data = {
        "username": "pet@example.com",
        "password": "54545"
    }
    login_response = await async_client.post("/auth/login", data=login_data)
    token = login_response.json()["access_token"]

    breed_data = {
        "name": "Labrador",
        "img": "labrador.jpg",
        "description": "Friendly dog breed"
    }

    breed_response = await async_client.post(
        "/breeds/",
        json=breed_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    breed_id = breed_response.json()["id"]

    pet_data = {
        "name": "Raplh",
        "gender": "M",
        "birth_date": "2024-11-01",
        "breed_id": breed_id
    }

    response = await async_client.post(
        "/pets/",
        json=pet_data,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Raplh"
    assert "id" in data