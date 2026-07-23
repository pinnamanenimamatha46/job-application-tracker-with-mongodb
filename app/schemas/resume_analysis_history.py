from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.resume_analysis import ResumeAnalysis


class ResumeAnalysisHistory(BaseModel):
    id: str
    resume_filename: str
    job_description: str
    analysis: ResumeAnalysis
    created_at: datetime


class ResumeAnalysisHistoryList(BaseModel):
    items: list[ResumeAnalysisHistory] = Field(
        default_factory=list
    )
    total: int