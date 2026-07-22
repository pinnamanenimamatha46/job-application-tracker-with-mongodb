from typing import Any

from fastapi import APIRouter, HTTPException, status

from app.repositories.application_repository import job_application_repository
from app.schemas.application import JobApplicationCreate


router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def create_application(
    application: JobApplicationCreate,
) -> dict[str, Any]:
    try:
        return await job_application_repository.create(application)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create job application.",
        ) from exc


@router.get("")
async def list_applications() -> list[dict[str, Any]]:
    return await job_application_repository.get_all()


@router.get("/{application_id}")
async def get_application(
    application_id: str,
) -> dict[str, Any]:
    application = await job_application_repository.get_by_id(application_id)

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found.",
        )

    return application