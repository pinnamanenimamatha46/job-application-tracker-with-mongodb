from pydantic import BaseModel, Field


class ResumeAnalysisRequest(BaseModel):
    resume_path: str = Field(
        ...,
        description="Path to the resume file",
    )
    job_description: str = Field(
        ...,
        min_length=20,
        description="Job description text",
    )