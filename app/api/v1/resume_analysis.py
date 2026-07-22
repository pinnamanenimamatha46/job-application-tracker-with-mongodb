from fastapi import APIRouter, HTTPException, status
from openai import OpenAIError

from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.resume_request import ResumeAnalysisRequest
from app.services.resume_analysis_service import analyze_resume_match


router = APIRouter(
    prefix="/resume-analysis",
    tags=["Resume Analysis"],
)


@router.post(
    "",
    response_model=ResumeAnalysis,
    status_code=status.HTTP_200_OK,
)
def analyze_resume(
    request: ResumeAnalysisRequest,
) -> ResumeAnalysis:
    """Compare resume text with a job description."""
    try:
        return analyze_resume_match(
            resume_text=request.resume_text,
            job_description=request.job_description,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except OpenAIError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The AI service could not complete the analysis.",
        ) from exc
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc