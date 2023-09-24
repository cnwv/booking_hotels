from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import time
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
from app.logger import logger
from redis import asyncio as aioredis
import sentry_sdk
from prometheus_fastapi_instrumentator import Instrumentator
from app.database import engine
from app.users.models import Users

app = FastAPI()
sentry_sdk.init(
    dsn="https://5d5ac986df96beb95a2553c412fe0662@o4505913458425856.ingest.sentry.io/4505913475989504",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
app.include_router(router_bookings)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_page)
app.include_router(router_images)

app.mount("/static", StaticFiles(directory="app/static"), "static")


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}/{settings.REDIS_HOST}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")


instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"]
)

instrumentator.instrument(app).expose(app)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })
    return response


admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(BookingsAdmin)
