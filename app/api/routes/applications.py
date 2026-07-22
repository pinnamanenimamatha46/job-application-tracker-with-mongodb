from fastapi import APIRouter, HTTPException, Query, Response, status

from app.repositories.application_repository import (
    job_application_repository,
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
    created = await job_application_repository.create(application)

    return JobApplicationResponse.model_validate(created)


@router.get(
    "",
    response_model=list[JobApplicationResponse],
)
async def get_job_applications(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[JobApplicationResponse]:
    applications = await job_application_repository.get_all(
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
    application = await job_application_repository.get_by_id(
        application_id
    )

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
    updated = await job_application_repository.update(
        application_id,
        application,
    )

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found",
        )

    return JobApplicationResponse.model_validate(updated)


@router.delete(
    "/{application_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def remove_job_application(
    application_id: str,
) -> Response:
    deleted = await job_application_repository.delete(application_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)