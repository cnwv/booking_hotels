import asyncio
from datetime import date, datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Query

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotelInfo, SHotelModel, SHotel
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{location}")
@cache(expire=60)
async def get_hotels_by_location_and_time(
        location: str,
        date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
        date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SHotelInfo]:
    await asyncio.sleep(3)
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    return hotels


@router.post("")
async def add_hotel(data: SHotelModel):
    await HotelDAO.add(dict(data))


@router.patch("{hotel_id}")
async def update_hotel(hotel_id: int, data: SHotelModel):
    await HotelDAO.update(hotel_id, dict(data))


@router.delete("{hotel_id}")
async def delete_hotel(hotel_id: int):
    await HotelDAO.delete(id=hotel_id)

