import pytest
from httpx import AsyncClient


# @pytest.mark
async def test_add_and_get_booking(authenticated_ac: AsyncClient):
    response = await authenticated_ac.post("/bookings", params={
    })
