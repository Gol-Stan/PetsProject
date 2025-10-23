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
        "email": "login@example.com",
        "password": "54545"
    }
    login_response = await async_client.post("/auth/login", data=login_data)
    token = login_response.json()["access_token"]

    pet_data = {
        "name": "Raplh",
        "gender": "M",
        "birth_date": "01.11.2024",
        "breed_id": 1
    }

    response = await async_client.post("/pets", json=pet_data, headers = {"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

