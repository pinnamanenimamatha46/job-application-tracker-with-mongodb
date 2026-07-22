from datetime import date, datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class ApplicationStatus(StrEnum):
    SAVED = "saved"
    APPLIED = "applied"
    SCREENING = "screening"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


class WorkMode(StrEnum):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"


class JobApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=150)
    position: str = Field(min_length=1, max_length=150)

    job_url: HttpUrl | None = None
    location: str | None = Field(default=None, max_length=150)
    work_mode: WorkMode | None = None

    status: ApplicationStatus = ApplicationStatus.SAVED
    applied_date: date | None = None

    salary_range: str | None = Field(default=None, max_length=100)
    skills: list[str] = Field(default_factory=list)
    job_description: str | None = None
    notes: str | None = None
    resume_version: str | None = Field(default=None, max_length=100)


class JobApplicationUpdate(BaseModel):
    company: str | None = Field(default=None, min_length=1, max_length=150)
    position: str | None = Field(default=None, min_length=1, max_length=150)

    job_url: HttpUrl | None = None
    location: str | None = Field(default=None, max_length=150)
    work_mode: WorkMode | None = None

    status: ApplicationStatus | None = None
    applied_date: date | None = None

    salary_range: str | None = Field(default=None, max_length=100)
    skills: list[str] | None = None
    job_description: str | None = None
    notes: str | None = None
    resume_version: str | None = Field(default=None, max_length=100)


class JobApplicationResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={HttpUrl: str},
    )

    id: str
    company: str
    position: str

    job_url: str | None = None
    location: str | None = None
    work_mode: WorkMode | None = None

    status: ApplicationStatus
    applied_date: date | None = None

    salary_range: str | None = None
    skills: list[str] = Field(default_factory=list)
    job_description: str | None = None
    notes: str | None = None
    resume_version: str | None = None

    created_at: datetime
    updated_at: datetime