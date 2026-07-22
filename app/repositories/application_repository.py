from datetime import UTC, datetime
from typing import Any

from bson import ObjectId
from pymongo import DESCENDING

from app.database.mongodb import database
from app.schemas.application import (
    JobApplicationCreate,
    JobApplicationUpdate,
)


COLLECTION_NAME = "job_applications"


def get_collection():
    """Return the MongoDB job applications collection."""
    return database[COLLECTION_NAME]


def serialize_application(document: dict[str, Any]) -> dict[str, Any]:
    """Convert a MongoDB document into an API-friendly dictionary."""
    return {
        "id": str(document["_id"]),
        "company": document["company"],
        "position": document["position"],
        "job_url": document.get("job_url"),
        "location": document.get("location"),
        "work_mode": document.get("work_mode"),
        "status": document.get("status", "saved"),
        "applied_date": document.get("applied_date"),
        "salary_range": document.get("salary_range"),
        "skills": document.get("skills", []),
        "job_description": document.get("job_description"),
        "notes": document.get("notes"),
        "resume_version": document.get("resume_version"),
        "created_at": document["created_at"],
        "updated_at": document["updated_at"],
    }


def to_object_id(application_id: str) -> ObjectId | None:
    """Convert a string ID to a MongoDB ObjectId."""
    if not ObjectId.is_valid(application_id):
        return None

    return ObjectId(application_id)


async def create_application(
    application: JobApplicationCreate,
) -> dict[str, Any]:
    """Create a job application."""
    now = datetime.now(UTC)

    document = application.model_dump(mode="json")
    document["created_at"] = now
    document["updated_at"] = now

    result = await get_collection().insert_one(document)

    created_document = await get_collection().find_one(
        {"_id": result.inserted_id}
    )

    if created_document is None:
        raise RuntimeError("The job application could not be retrieved")

    return serialize_application(created_document)


async def list_applications(
    skip: int = 0,
    limit: int = 20,
) -> list[dict[str, Any]]:
    """Return job applications ordered by newest first."""
    cursor = (
        get_collection()
        .find()
        .sort("created_at", DESCENDING)
        .skip(skip)
        .limit(limit)
    )

    applications: list[dict[str, Any]] = []

    async for document in cursor:
        applications.append(serialize_application(document))

    return applications


async def get_application(
    application_id: str,
) -> dict[str, Any] | None:
    """Return one job application by ID."""
    object_id = to_object_id(application_id)

    if object_id is None:
        return None

    document = await get_collection().find_one({"_id": object_id})

    if document is None:
        return None

    return serialize_application(document)


async def update_application(
    application_id: str,
    application: JobApplicationUpdate,
) -> dict[str, Any] | None:
    """Update an existing job application."""
    object_id = to_object_id(application_id)

    if object_id is None:
        return None

    update_data = application.model_dump(
        mode="json",
        exclude_unset=True,
    )

    if not update_data:
        return await get_application(application_id)

    update_data["updated_at"] = datetime.now(UTC)

    result = await get_collection().update_one(
        {"_id": object_id},
        {"$set": update_data},
    )

    if result.matched_count == 0:
        return None

    return await get_application(application_id)


async def delete_application(application_id: str) -> bool:
    """Delete a job application by ID."""
    object_id = to_object_id(application_id)

    if object_id is None:
        return False

    result = await get_collection().delete_one({"_id": object_id})

    return result.deleted_count == 1