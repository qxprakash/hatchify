from fastapi import APIRouter
from src.service.health_service import HealthService

router = APIRouter()

@router.get("/health")
async def health_check():
    return await HealthService.check_health()