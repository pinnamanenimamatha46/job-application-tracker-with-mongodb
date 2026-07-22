from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="AI Job Application Tracker",
    description=(
        "Full Stack Generative AI and Agentic AI "
        "Job Application Tracking Platform"
    ),
    version="0.1.0",
)

# Register all API routes
app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to the AI Job Application Tracker API",
        "status": "running",
        "version": "0.1.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


@app.get("/api/v1/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "AI Job Application Tracker",
        "database": "job_application_tracker",
    }