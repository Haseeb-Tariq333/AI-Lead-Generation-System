from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config.settings import settings
from app.db.session import get_db

app = FastAPI(title=settings.app_name)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }


@app.get("/api/health/db")
def database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"database": "ok"}
    except Exception:
        raise HTTPException(status_code=503, detail="Database unavailable")