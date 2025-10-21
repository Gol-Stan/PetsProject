import pytest

@pytest.mark.asyncio
async def test_register_user_async(async_client):
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "123"
    }
    response = await async_client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert "id" in data