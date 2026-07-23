from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.ai.resume_matcher import analyze_resume_match, extract_resume_text
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


class ResumeMatchRequest(BaseModel):
    resume_text: str = Field(min_length=1)
    job_description: str = Field(min_length=1)


@router.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "Resume AI",
    }


@router.post(
    "/analyze",
    response_model=ResumeAnalysis,
)
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


@router.post(
    "/upload-analyze",
    response_model=ResumeAnalysisHistory,
)
async def upload_and_analyze_resume(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...),
) -> ResumeAnalysisHistory:
    filename = resume_file.filename or ""
    suffix = Path(filename).suffix.lower()

    if suffix not in {".pdf", ".docx", ".txt"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, and TXT resume files are supported.",
        )

    temporary_path: Path | None = None

    try:
        file_content = await resume_file.read()

        if not file_content:
            raise HTTPException(
                status_code=400,
                detail="The uploaded resume file is empty.",
            )

        if not job_description.strip():
            raise HTTPException(
                status_code=400,
                detail="Job description cannot be empty.",
            )

        with NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as temporary_file:
            temporary_file.write(file_content)
            temporary_path = Path(temporary_file.name)

        resume_text = extract_resume_text(temporary_path)

        analysis = analyze_resume_match(
            resume_text=resume_text,
            job_description=job_description,
        )

        saved_analysis = await resume_analysis_repository.create(
            resume_filename=filename,
            job_description=job_description,
            analysis=analysis,
        )

        return ResumeAnalysisHistory.model_validate(saved_analysis)

    except HTTPException:
        raise
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Resume upload analysis failed.",
        ) from exc
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


@router.get(
    "/history",
    response_model=ResumeAnalysisHistoryList,
)
async def get_resume_analysis_history() -> ResumeAnalysisHistoryList:
    analyses = await resume_analysis_repository.get_all()

    return ResumeAnalysisHistoryList(
        items=[
            ResumeAnalysisHistory.model_validate(analysis)
            for analysis in analyses
        ],
        total=len(analyses),
    )


@router.get(
    "/history/{analysis_id}",
    response_model=ResumeAnalysisHistory,
)
async def get_resume_analysis(
    analysis_id: str,
) -> ResumeAnalysisHistory:
    analysis = await resume_analysis_repository.get_by_id(analysis_id)

    if analysis is None:
        raise HTTPException(
            status_code=404,
            detail="Resume analysis not found.",
        )

    return ResumeAnalysisHistory.model_validate(analysis)


@router.delete(
    "/history/{analysis_id}",
    status_code=204,
)
async def delete_resume_analysis(
    analysis_id: str,
) -> None:
    deleted = await resume_analysis_repository.delete(analysis_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Resume analysis not found.",
        )