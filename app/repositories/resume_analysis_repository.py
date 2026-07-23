from datetime import UTC, datetime
from typing import Any

from bson import ObjectId

from app.database.mongodb import database
from app.schemas.resume_analysis import ResumeAnalysis


class ResumeAnalysisRepository:
    """MongoDB repository for resume analysis history."""

    def __init__(self) -> None:
        self.collection = database["resume_analyses"]

    @staticmethod
    def serialize(document: dict[str, Any]) -> dict[str, Any]:
        """Convert MongoDB values into JSON-compatible values."""
        document["id"] = str(document.pop("_id"))
        return document

    async def create(
        self,
        resume_filename: str,
        job_description: str,
        analysis: ResumeAnalysis,
    ) -> dict[str, Any]:
        """Save a resume analysis result."""
        document = {
            "resume_filename": resume_filename,
            "job_description": job_description,
            "analysis": analysis.model_dump(),
            "created_at": datetime.now(UTC),
        }

        result = await self.collection.insert_one(document)

        saved_document = await self.collection.find_one(
            {"_id": result.inserted_id}
        )

        if saved_document is None:
            raise RuntimeError("Resume analysis could not be saved.")

        return self.serialize(saved_document)

    async def get_all(self) -> list[dict[str, Any]]:
        """Return all resume analyses, newest first."""
        cursor = self.collection.find().sort("created_at", -1)

        documents = await cursor.to_list(length=100)

        return [
            self.serialize(document)
            for document in documents
        ]

    async def get_by_id(
        self,
        analysis_id: str,
    ) -> dict[str, Any] | None:
        """Return one resume analysis by MongoDB ID."""
        if not ObjectId.is_valid(analysis_id):
            return None

        document = await self.collection.find_one(
            {"_id": ObjectId(analysis_id)}
        )

        if document is None:
            return None

        return self.serialize(document)

    async def delete(self, analysis_id: str) -> bool:
        """Delete one saved resume analysis."""
        if not ObjectId.is_valid(analysis_id):
            return False

        result = await self.collection.delete_one(
            {"_id": ObjectId(analysis_id)}
        )

        return result.deleted_count == 1


resume_analysis_repository = ResumeAnalysisRepository()