from fastapi import APIRouter
from .health import router as health_router
from .publish import router as publish_router

router = APIRouter()

router.include_router(health_router, tags=["health"])
router.include_router(publish_router, tags=["publish"])