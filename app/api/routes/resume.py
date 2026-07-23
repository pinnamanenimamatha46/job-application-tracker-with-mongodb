from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.ai.resume_matcher import (
    ResumeAnalysis,
    analyze_resume_match,
    extract_resume_text,
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


@router.post("/upload-analyze", response_model=ResumeAnalysis)
async def upload_and_analyze_resume(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...),
) -> ResumeAnalysis:
    filename = resume_file.filename or ""

    suffix = Path(filename).suffix.lower()

    if suffix not in {".pdf", ".docx"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX resume files are supported.",
        )

    try:
        file_content = await resume_file.read()

        if not file_content:
            raise HTTPException(
                status_code=400,
                detail="The uploaded resume file is empty.",
            )

        with NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as temporary_file:
            temporary_file.write(file_content)
            temporary_path = Path(temporary_file.name)

        resume_text = extract_resume_text(temporary_path)

        return analyze_resume_match(
            resume_text=resume_text,
            job_description=job_description,
        )

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
        if "temporary_path" in locals():
            temporary_path.unlink(missing_ok=True)