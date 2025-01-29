from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime
from enum import Enum

class IndustryType(str, Enum):
    SAAS = "saas"
    ECOMMERCE = "ecommerce"
    MOBILE_APP = "mobile_app"
    MARKETPLACE = "marketplace"
    OTHER = "other"

class AppIdea(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=1000)
    industry: IndustryType
    target_audience: List[str]
    features: List[str]
    budget: Optional[float] = None
    timeline_months: Optional[int] = Field(None, ge=1, le=24)

class CompetitorInfo(BaseModel):
    name: str
    website: HttpUrl
    key_features: List[str]
    market_share: Optional[float] = None

class MarketAnalysis(BaseModel):
    market_size: float
    growth_rate: float
    competitors: List[CompetitorInfo]
    risks: List[str]
    opportunities: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TechStackRecommendation(BaseModel):
    frontend: List[str]
    backend: List[str]
    database: List[str]
    infrastructure: List[str]
    estimated_cost: float