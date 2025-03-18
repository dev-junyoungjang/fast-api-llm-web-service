from fastapi import FastAPI
from api.endpoints import items
from api.endpoints import health
from api.routers import api_router

app = FastAPI(
    title="LLM service api",
    description="LLM service api",
    version="1.0.0",
)

app.include_router(api_router, prefix="")