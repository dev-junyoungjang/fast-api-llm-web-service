from fastapi import APIRouter
from api.endpoints import items
from api.endpoints import health

api_router = APIRouter()

api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(health.router, prefix="/health", tags=["health"])