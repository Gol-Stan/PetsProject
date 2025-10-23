import pytest

@pytest.mark.asyncio
async def test_register_user_async(async_client):
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "12345"
    }
    response = await async_client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert "id" in data

@pytest.mark.asyncio
async def test_login_user(async_client):
    user_data = {
        "name": "Test User",
        "email": "login@example.com",
        "password": "54321"
    }
    await async_client.post("/auth/register", json=user_data)

    login_data = {
        "email": "login@example.com",
        "password": "54321"
    }
    response = await async_client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

