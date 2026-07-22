from fastapi import APIRouter, HTTPException, Query, Response, status

from app.repositories.application_repository import (
    create_application,
    delete_application,
    get_application,
    list_applications,
    update_application,
)
from app.schemas.application import (
    JobApplicationCreate,
    JobApplicationResponse,
    JobApplicationUpdate,
)


router = APIRouter(
    prefix="/applications",
    tags=["Job Applications"],
)


@router.post(
    "",
    response_model=JobApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_job_application(
    application: JobApplicationCreate,
) -> JobApplicationResponse:
    """Create a new job application."""
    created_application = await create_application(application)

    return JobApplicationResponse.model_validate(created_application)


@router.get(
    "",
    response_model=list[JobApplicationResponse],
)
async def get_job_applications(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[JobApplicationResponse]:
    """Return job applications ordered by newest first."""
    applications = await list_applications(
        skip=skip,
        limit=limit,
    )

    return [
        JobApplicationResponse.model_validate(application)
        for application in applications
    ]


@router.get(
    "/{application_id}",
    response_model=JobApplicationResponse,
)
async def get_job_application(
    application_id: str,
) -> JobApplicationResponse:
    """Return one job application."""
    application = await get_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found",
        )

    return JobApplicationResponse.model_validate(application)


@router.patch(
    "/{application_id}",
    response_model=JobApplicationResponse,
)
async def update_job_application(
    application_id: str,
    application: JobApplicationUpdate,
) -> JobApplicationResponse:
    """Partially update a job application."""
    updated_application = await update_application(
        application_id=application_id,
        application=application,
    )

    if updated_application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found",
        )

    return JobApplicationResponse.model_validate(updated_application)


@router.delete(
    "/{application_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def remove_job_application(
    application_id: str,
) -> Response:
    """Delete a job application."""
    deleted = await delete_application(application_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)