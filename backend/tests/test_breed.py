import pytest

@pytest.mark.asyncio
async def test_breed_create(async_client):
    admin_data = {
        'name': 'Admin',
        'email': 'admin@example.com',
        'password': '98765',
        'is_admin': True
    }
    await async_client.post('/auth/register', json=admin_data)

    login_data = {
        'email': 'admin@example.com',
        'password': '98765'
    }
    login_response = await async_client.post('/auth/login', data=login_data)
    token = login_response.json()["access_toke"]

    breed_data = {
        'name': 'Retriever',
        'img': 'test.jpg',
        'description': 'friendly and beautiful'
    }
    response = await async_client.post("/breeds/", json=breed_data, header={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'Retriever'

@pytest.mark.asyncio
async def test_no_admin_create(async_client):
    admin_data = {
        'name': 'Admin',
        'email': 'admin@example.com',
        'password': '98765',
        'is_admin': False
    }
    await async_client.post('/auth/register', json=admin_data)

    login_data = {
        'email': 'admin@example.com',
        'password': '98765'
    }
    login_response = await async_client.post('/auth/login', data=login_data)
    token = login_response.json()["access_toke"]

    breed_data = {
        'name': 'Retriever',
        'img': 'test.jpg',
        'description': 'friendly and beautiful'
    }
    response = await async_client.post("/breeds/", json=breed_data, header={'Authorization': f'Bearer {token}'})
    assert response.status_code == 403
    assert "Not enough permissions" in response.json()["detail"]


@pytest.mark.asyncio
async def test_create_breed_without_auth(async_client):
    breed_data = {
        "name": "Test Breed",
        "img": "test.jpg",
        "description": "Test description"
    }

    response = await async_client.post("/breeds/", json=breed_data)
    assert response.status_code == 401
