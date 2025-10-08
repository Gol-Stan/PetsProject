from http.client import responses

import pytest
from app.schemas.pet import PetBase
import datetime

@pytest.mark.asyncio
async def test_create_pet(client):
    await client.post("/auth/register", json={"name": "Owner", "email": "owner@mail.com", "password": "secret"})
    login = await client.post("auth/login", data={"username": "owner@mail.com", "password": "secret"})
    token = login.json()["access_token"]

    pet_data = {
        "name": "Ralph",
        "gender": "M",
        "birth_date": str(datetime.date.today()),
        "breed_id": 1,
        "vaccine": "needed",
        "img": "img_url",
        "qr_code": "placeholder"
    }

    headers = {"Authorisation": f'Bearer {token}'}
    response = await client.post("/pets", json=pet_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ralph"

