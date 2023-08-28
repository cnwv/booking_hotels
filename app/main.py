from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.pages.router import router as router_page
from app.images.router import router as router_images
from app.hotels.rooms.router import *
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

app = FastAPI()

app.include_router(router_bookings)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_page)
app.include_router(router_images)


app.mount("/static", StaticFiles(directory="app/static"), "static")

