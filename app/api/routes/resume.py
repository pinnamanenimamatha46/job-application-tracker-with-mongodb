from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.ai.resume_matcher import analyze_resume_match
from app.repositories.resume_analysis_repository import (
    resume_analysis_repository,
)
from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.resume_analysis_history import (
    ResumeAnalysisHistory,
    ResumeAnalysisHistoryList,
)


router = APIRouter(
    prefix="/resume",
    tags=["Resume AI"],
)

@router.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "Resume AI",
    }