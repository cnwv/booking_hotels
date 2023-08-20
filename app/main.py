from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_bookings)

class HotelSearchAgrs:
    def __init__(self,
                 location: str,
                 date_from: date,
                 date_to: date,
                 has_spa: Optional[bool] = Query(None),
                 stars: Optional[int] = Query(None, ge=1, le=5)
                 ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int
    has_spa: Optional[bool] = Query(None)


@app.get('/hotels/')  # , response_model=list[SHotel]
def get_hotels(
        search_args: HotelSearchAgrs = Depends()

) -> list[SHotel]:
    hotels = [
        {
            "address": "ул. Советская, 1, Батуми",
            "name": "Super Hotel",
            "stars": 1
        },
        {
            "address": "ул. Советская, 1, Батуми",
            "name": "Super Hotel",
            "stars": 1
        },
        {
            "address": "ул. Советская, 1, Батуми",
            "name": "Super Hotel",
            "stars": 1
        },
        {
            "address": "ул. Советская, 1, Батуми",
            "name": "Super Hotel",
            "stars": 1
        },

    ]
    return hotels


@app.get('/hotels/{hotel_id}')
def get_hotels(hotel_id, date_from, date_to):
    return hotel_id, date_from, date_to


class SBookingPost(BaseModel):
    room_id: int
    date_from: date
    date_to: date


# @app.post("/bookings")
# def add_booking(booking: SBookingPost):
#     return booking
