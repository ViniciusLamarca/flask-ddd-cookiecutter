"""Pydantic schemas for API request/response validation."""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response schema."""
    
    status: str
    service: str

