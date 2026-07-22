from fastapi import FastAPI

from app.api.v1.applications import router as applications_router


app = FastAPI(
    title="Job Application Tracker API",
    description="Full-stack job application tracker using FastAPI and MongoDB",
    version="0.1.0",
)


app.include_router(
    applications_router,
    prefix="/api/v1",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Job Application Tracker API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/api/v1/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "job-application-tracker",
        "database": "MongoDB",
    }
