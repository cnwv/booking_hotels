from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.admin.auth import authentication_backend
from app.admin.views import UsersAdmin, BookingsAdmin, HotelsAdmin, RoomsAdmin
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.pages.router import router as router_page
from app.images.router import router as router_images
from app.hotels.rooms.router import *
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from app.config import settings
from sqladmin import Admin, ModelView

from redis import asyncio as aioredis

from app.database import engine
from app.users.models import Users

app = FastAPI()
app.include_router(router_bookings)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_page)
app.include_router(router_images)

app.mount("/static", StaticFiles(directory="app/static"), "static")


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}/{settings.REDIS_HOST}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")


admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(BookingsAdmin)
