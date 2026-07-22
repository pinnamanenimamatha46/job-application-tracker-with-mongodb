from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.ai.resume_matcher import ResumeAnalysis, analyze_resume_match

router = APIRouter(
    prefix="/resume",
    tags=["Resume AI"],
)


class ResumeMatchRequest(BaseModel):
    resume_text: str = Field(min_length=1)
    job_description: str = Field(min_length=1)


@router.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "Resume AI",
    }


@router.post("/analyze", response_model=ResumeAnalysis)
async def analyze_resume(
    request: ResumeMatchRequest,
) -> ResumeAnalysis:
    try:
        return analyze_resume_match(
            resume_text=request.resume_text,
            job_description=request.job_description,
        )
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Resume analysis failed.",
        ) from exc