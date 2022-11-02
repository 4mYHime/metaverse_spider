from fastapi import APIRouter

from api.api_v1.spider import router as spider_router

api_v1_router = APIRouter()
api_v1_router.include_router(spider_router, tags=["spider"])
