from datetime import datetime, timezone
from typing import Any

from bson import ObjectId

from app.database.mongodb import database
from app.schemas.application import JobApplicationCreate


class JobApplicationRepository:
    def __init__(self) -> None:
        self.collection = database["job_applications"]

    @staticmethod
    def serialize(document: dict[str, Any]) -> dict[str, Any]:
        document["_id"] = str(document["_id"])
        return document

    async def create(
        self,
        application: JobApplicationCreate,
    ) -> dict[str, Any]:
        now = datetime.now(timezone.utc)

        document = application.model_dump(mode="json")
        document["created_at"] = now
        document["updated_at"] = now

        result = await self.collection.insert_one(document)

        created_application = await self.collection.find_one(
            {"_id": result.inserted_id}
        )

        if created_application is None:
            raise RuntimeError(
                "The application was inserted but could not be retrieved."
            )

        return self.serialize(created_application)

    async def get_all(self) -> list[dict[str, Any]]:
        applications: list[dict[str, Any]] = []

        cursor = self.collection.find().sort("created_at", -1)

        async for application in cursor:
            applications.append(self.serialize(application))

        return applications

    async def get_by_id(
        self,
        application_id: str,
    ) -> dict[str, Any] | None:
        if not ObjectId.is_valid(application_id):
            return None

        application = await self.collection.find_one(
            {"_id": ObjectId(application_id)}
        )

        if application is None:
            return None

        return self.serialize(application)


job_application_repository = JobApplicationRepository()