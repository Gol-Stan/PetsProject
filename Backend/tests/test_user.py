import pytest_asyncio
import pytest

@pytest.mark.asyncio
async def test_register_user(client):
    user_data = {"name": "Stan", "email": "stan@test.com", "password": "secret"}
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Stan"
    assert "id" in data


@pytest.mark.asyncio
async def test_login_user(client):

    await client.post("/auth/register", json={
        "name": "Any",
        "email": "any@test.com",
        "password": "secret"
    })


    login_data = {"username": "any@test.com", "password": "secret"}
    response = await client.post("/auth/login", data=login_data)

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data