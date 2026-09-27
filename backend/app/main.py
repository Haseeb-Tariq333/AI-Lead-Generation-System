from fastapi import FastAPI

from app.config.settings import settings

app = FastAPI(title=settings.app_name)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }