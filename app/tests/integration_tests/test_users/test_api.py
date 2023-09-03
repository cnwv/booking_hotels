from httpx import AsyncClient
import pytest


@pytest.mark.parametrize(
    "email,password,status_code",
    [("dog@test.com", "test", 200),
     ("wrong_email", "test", 422),
     ("dog@test.com", "test", 409)])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={"email": email, "password": password}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [("test@test.com", "test", 200),
     ("artem@example.com", "artem", 200),
     ("wrong@person.com", "test", 401)
     ]
)
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/login",
        json={"email": email, "password": password}
    )
    assert response.status_code == status_code
