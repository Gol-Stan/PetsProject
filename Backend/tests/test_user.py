import pytest
from app import models

@pytest.mark.asyncio
async def test_register_user(client):
    user_data = {
        "name": "Stan",
        "email": "stan@test.com",
        "password": "12345",
        "phone": "123456789"
    }
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data ["name"] == "Stan"
    assert data ["email"] == "stan@test.com"
    assert "id" in data
    assert "hashed_password" not in data

@pytest.mark.asyncio
async def test_register_duplicate_email(client):
    user_data = {
        "name": "John",
        "email": "john@test.com",
        "password": "s12345"
    }

    response1 = await client.post("/auth/register", json=user_data)
    assert response1.status_code == 201

    response2 = await client.post("/auth/register", json=user_data)
    assert  response2.status_code == 400
    assert "already" in response2.json()["detail"].lower()