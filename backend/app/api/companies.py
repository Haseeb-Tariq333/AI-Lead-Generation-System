from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Company
from app.schemas.company import CompanyListResponse, CompanyRead

router = APIRouter(prefix="/api/companies", tags=["companies"])


@router.get("", response_model=CompanyListResponse)
def list_companies(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    total = db.scalar(select(func.count()).select_from(Company))

    companies = db.scalars(
        select(Company).order_by(Company.id).limit(limit).offset(offset)
    ).all()

    return CompanyListResponse(
        items=[CompanyRead.model_validate(company) for company in companies],
        total=total,
        limit=limit,
        offset=offset,
    )