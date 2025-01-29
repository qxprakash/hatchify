from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from src.service.publish_service import PublishService

class IdeaRequest(BaseModel):
    title: str
    description: str
    features: List[str]

router = APIRouter()

@router.post("/publish")
async def publish_idea(idea: IdeaRequest):
    return await PublishService.publish_idea(idea.model_dump())