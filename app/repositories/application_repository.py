from datetime import datetime, timezone
from typing import Any

from bson import ObjectId

from app.database.mongodb import database
from app.schemas.application import (
    JobApplicationCreate,
    JobApplicationUpdate,
)


class JobApplicationRepository:
    def __init__(self) -> None:
        self.collection = database["job_applications"]

    @staticmethod
    def serialize(document: dict[str, Any]) -> dict[str, Any]:
        serialized = document.copy()
        serialized["id"] = str(serialized.pop("_id"))
        return serialized

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

    async def get_all(
        self,
        skip: int = 0,
        limit: int = 20,
    ) -> list[dict[str, Any]]:
        applications: list[dict[str, Any]] = []

        cursor = (
            self.collection
            .find()
            .sort("created_at", -1)
            .skip(skip)
            .limit(limit)
        )

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

    async def update(
        self,
        application_id: str,
        application: JobApplicationUpdate,
    ) -> dict[str, Any] | None:
        if not ObjectId.is_valid(application_id):
            return None

        update_data = application.model_dump(
            mode="json",
            exclude_unset=True,
        )

        if not update_data:
            return await self.get_by_id(application_id)

        update_data["updated_at"] = datetime.now(timezone.utc)

        result = await self.collection.update_one(
            {"_id": ObjectId(application_id)},
            {"$set": update_data},
        )

        if result.matched_count == 0:
            return None

        return await self.get_by_id(application_id)

    async def delete(
        self,
        application_id: str,
    ) -> bool:
        if not ObjectId.is_valid(application_id):
            return False

        result = await self.collection.delete_one(
            {"_id": ObjectId(application_id)}
        )

        return result.deleted_count == 1


job_application_repository = JobApplicationRepository()