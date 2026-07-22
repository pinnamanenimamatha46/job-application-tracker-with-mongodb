from fastapi import APIRouter

from app.api.routes.applications import router as applications_router
from app.api.routes.resume import router as resume_router

api_router = APIRouter()

api_router.include_router(applications_router)
api_router.include_router(resume_router)



