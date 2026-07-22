from typing import Any

import pytest
from httpx import AsyncClient


APPLICATION_PAYLOAD: dict[str, Any] = {
    "company": "Microsoft",
    "position": "AI Software Engineer",
    "job_url": "https://careers.microsoft.com",
    "location": "Redmond, WA",
    "work_mode": "hybrid",
    "status": "applied",
    "applied_date": "2026-07-22",
    "salary_range": "$140,000-$180,000",
    "skills": [
        "Python",
        "FastAPI",
        "MongoDB",
        "Azure",
        "Docker",
        "Agentic AI",
    ],
    "job_description": (
        "Develop AI-powered enterprise applications."
    ),
    "notes": "Applied through Microsoft Careers.",
    "resume_version": "Full-Stack-AI-Resume-v1",
}


async def create_test_application(
    client: AsyncClient,
) -> dict[str, Any]:
    response = await client.post(
        "/api/v1/applications",
        json=APPLICATION_PAYLOAD,
    )

    assert response.status_code == 201

    return response.json()


@pytest.mark.asyncio
async def test_create_application(
    client: AsyncClient,
) -> None:
    response = await client.post(
        "/api/v1/applications",
        json=APPLICATION_PAYLOAD,
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"]
    assert data["company"] == "Microsoft"
    assert data["position"] == "AI Software Engineer"
    assert data["status"] == "applied"
    assert data["work_mode"] == "hybrid"
    assert "Python" in data["skills"]
    assert data["created_at"]
    assert data["updated_at"]


@pytest.mark.asyncio
async def test_list_applications(
    client: AsyncClient,
) -> None:
    created_application = await create_test_application(client)

    response = await client.get(
        "/api/v1/applications"
    )

    assert response.status_code == 200

    applications = response.json()

    assert len(applications) == 1
    assert applications[0]["id"] == created_application["id"]
    assert applications[0]["company"] == "Microsoft"


@pytest.mark.asyncio
async def test_get_application_by_id(
    client: AsyncClient,
) -> None:
    created_application = await create_test_application(client)
    application_id = created_application["id"]

    response = await client.get(
        f"/api/v1/applications/{application_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == application_id
    assert data["company"] == "Microsoft"
    assert data["position"] == "AI Software Engineer"


@pytest.mark.asyncio
async def test_update_application(
    client: AsyncClient,
) -> None:
    created_application = await create_test_application(client)
    application_id = created_application["id"]

    update_payload = {
        "status": "interview",
        "notes": "Initial HR interview scheduled.",
    }

    response = await client.patch(
        f"/api/v1/applications/{application_id}",
        json=update_payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == application_id
    assert data["status"] == "interview"
    assert data["notes"] == "Initial HR interview scheduled."
    assert data["company"] == "Microsoft"


@pytest.mark.asyncio
async def test_delete_application(
    client: AsyncClient,
) -> None:
    created_application = await create_test_application(client)
    application_id = created_application["id"]

    delete_response = await client.delete(
        f"/api/v1/applications/{application_id}"
    )

    assert delete_response.status_code == 204

    get_response = await client.get(
        f"/api/v1/applications/{application_id}"
    )

    assert get_response.status_code == 404
    assert get_response.json() == {
        "detail": "Job application not found"
    }


@pytest.mark.asyncio
async def test_invalid_application_id_returns_404(
    client: AsyncClient,
) -> None:
    response = await client.get(
        "/api/v1/applications/not-a-valid-object-id"
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Job application not found"
    }


@pytest.mark.asyncio
async def test_create_application_validation_error(
    client: AsyncClient,
) -> None:
    invalid_payload = {
        "company": "",
        "position": "",
        "work_mode": "office",
        "status": "unknown",
    }

    response = await client.post(
        "/api/v1/applications",
        json=invalid_payload,
    )

    assert response.status_code == 422