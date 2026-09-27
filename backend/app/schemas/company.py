from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CompanyRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    domain: str | None
    website: str | None
    industry: str | None
    employee_count: int | None
    country: str | None
    city: str | None
    last_updated: datetime


class CompanyListResponse(BaseModel):
    items: list[CompanyRead]
    total: int
    limit: int
    offset: int