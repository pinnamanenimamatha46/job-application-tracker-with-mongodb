## Job-Application-Tracker-with-MongoDB

## Mangodb download and Installation.

## Step 1: Download MongoDB Community Server

## https://www.mongodb.com/try/download/community

## Select:

Version: Current
Platform: Windows
Package: MSI

Click Download.

## Step 2: Download MongoDB Shell (mongosh)

https://www.mongodb.com/try/download/shell

Choose:

Windows
MSI Installer

Download and install it.

## Step 3: Install in vscode- Mangodb

## winget install MongoDB.Server

## Step 4: Open Powershell as administrator on Windows:

## test mangodb:
    ## & "C:\Program Files\MongoDB\Server\8.3\bin\mongod.exe" --version

## Check whether the MongoDB service is running:

Get-Service MongoDB

## Add MongoDB to your PATH so you can run mongod from anywhere.
$env:Path += ";C:\Program Files\MongoDB\Server\8.3\bin"

## Test:

mongod --version
8.3.4

## Step 4: Install MongoDB.Shell : mongosh:

## winget install MongoDB.Shell

## path
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($userPath -notlike "*$mongoshFolder*") {
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$userPath;$mongoshFolder",
        "User"
    )
}

## Test MongoDB Shell directly
& "C:\Users\MAMATHA PINNAMANENI\AppData\Local\Programs\mongosh\mongosh.exe" --version

## Add it to the current path:
$env:Path += ";C:\Users\MAMATHA PINNAMANENI\AppData\Local\Programs\mongosh"

## Test
mongosh --version

## powershell
mongosh
test>
use job_application_tracker ## test db
switched to db job_application_tracker
job_application_tracker> db.applications.find().pretty()

job_application_tracker>

db.applications.insertOne({
  company: "Microsoft",
  position: "Full Stack AI Developer",
  status: "Applied",
  applied_date: new Date()
}) ## test mangosh

View saved record
db.applications.find().pretty()

## To exit MongoDB Shell:
exit

## Use this connection string in your browaer via compass:
mongodb://localhost:27017/job_application_tracker

## .env
MONGODB_URL=mongodb://localhost:27017
MONGODB_DATABASE=job_application_tracker

##*********************************************************************************                               ## Job-Application-Tracker-with-MongoDB
##*********************************************************************************
 Phase 1 — Verify MongoDB
## Step 1: Verify MongoDB Server
mongod --version
8.3.4

## check whether the MongoDB Windows service is running:
Get-Service *Mongo*
Get-Service MongoDB

## Step 2: Connect with MongoDB Shell
mongodb://localhost:27017/job_application_tracker
mongosh "mongodb://localhost:27017/job_application_tracker"

db.system_check.insertOne({
  status: "MongoDB connected",
  checked_at: new Date()
})
{
  acknowledged: true,
  insertedId: ObjectId('6a60134b6e9d6878434e30f5')
}

Read: mongosh
tett> 
db.system_check.find()
use job_application_tracker
.exit

## connect your git, github
Step-1: Initialize git:   git init

Step-2: Create .gitignore file:
.venv/
__pycache__/
.pytest_cache/
.env
.vscode/

Step-3: Create README.md:
# Job Application Tracker with MongoDB

## About This Project

Welcome! I'm **Mamatha Pinnamaneni**, a Full Stack AI Developer passionate about designing and building enterprise-grade AI applications using Python, FastAPI, MongoDB, Generative AI, Agentic AI, and modern DevOps practices.

This project is part of my **Enterprise AI Portfolio**, where I build production-ready applications that demonstrate clean architecture, scalable backend development, API design, database integration, automation, and AI-powered solutions.

---

## Project Overview

The **Job Application Tracker** is a REST API application that helps users efficiently manage their job search by tracking applications, companies, recruiters, interview schedules, application status, follow-ups, notes, and job offers.

The project follows enterprise software engineering best practices and is designed to scale with additional AI capabilities such as resume analysis, interview preparation, intelligent job matching, and automated application insights.

---

## Objectives

* Build a production-ready FastAPI application
* Integrate MongoDB using PyMongo
* Develop RESTful APIs following best practices
* Implement environment-based configuration
* Practice Git and GitHub workflows
* Use **uv** for Python package management
* Follow enterprise software architecture
* Create a portfolio-ready Full Stack AI project

---

## Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Database

* MongoDB
* PyMongo

### Configuration

* Pydantic Settings
* python-dotenv

### Development Tools

* uv
* Git
* GitHub
* VS Code

### Testing

* Pytest

### Planned Enhancements

* Docker
* GitHub Actions (CI/CD)
* Kubernetes
* OpenAI API
* LangChain
* LangGraph
* Agentic AI
* Prometheus
* Grafana
* Resume Parser
* AI Job Recommendation Engine

---

## Project Structure

```text
Job-Application-Tracker-with-MongoDB/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Getting Started

1. Clone the project.
2. Create a virtual environment using `uv`.
3. Install the required dependencies.
4. Configure the `.env` file.
5. Start the MongoDB server.
6. Launch the FastAPI application.
7. Test the APIs using Swagger UI.

---

## Future Roadmap

* User Authentication
* Role-Based Access Control
* Resume Upload
* Resume AI Analysis
* Interview Scheduler
* Email Notifications
* Analytics Dashboard
* AI Career Assistant
* Job Market Insights
* Cloud Deployment
* Monitoring and Observability

---

## About Me

I'm **Mamatha Pinnamaneni**, a Full Stack AI Developer focused on building scalable enterprise applications with modern AI technologies.

My areas of interest include:

* Artificial Intelligence
* Generative AI
* Agentic AI
* FastAPI
* Python
* MongoDB
* PostgreSQL
* Docker
* Kubernetes
* DevOps
* GitHub Actions
* REST APIs
* Enterprise Software Engineering

I enjoy creating practical AI solutions that solve real-world business problems while continuously expanding my knowledge of modern software engineering and AI technologies.

---

## Connect With Me

**GitHub**

https://github.com/pinnamanenimamatha46

**LinkedIn**

Add your LinkedIn profile URL here.

---

## License

This project is developed for learning, portfolio demonstration, and enterprise AI software engineering practices.

---

**Thank you for visiting this project. If you find it useful, feel free to explore my other AI projects and connect with me on GitHub.**


Ste-4: Create github project:    
job-application-tracker-with-mongodb

Step -5: Connect local to github

git branch -M main
git remote add origin https://github.com/pinnamanenimamatha46/job-application-tracker-with-mongodb.git
git push -u origin main

## Step - 6: create uv 

uv init --app --python 3.11

## Step-7: create env and activate it

uv venv .venv --python 3.11
.venv\Scripts\activate

## Step - 8: Check versions:

python --version    :   3.11.9
uv --version        :   0.11.18
node --version      :   24.15.0
npm --version       :   11.12.1
mongod --version    :   8.3.4
Mongosh             :   2.9.2

## step -9: Create C:\data\db
mongod --dbpath C:\data\db
New-Item -ItemType Directory -Path C:\data\db -Force
mongosh
test> 
show dbs
application connection string:
MONGODB_URL=mongodb://localhost:27017
MONGODB_DATABASE=job_application_tracker

## step-10: install the project dependencies:
uv add fastapi uvicorn motor pydantic-settings python-dotenv

## step-11: create the initial folders:
New-Item -ItemType Directory -Force `
    app, `
    app\api, `
    app\api\v1, `
    app\core, `
    app\database, `
    app\models, `
    app\repositories, `
    app\schemas, `
    app\services, `
    tests

## step-12: Create the Python package files:

## Build the configuration and MongoDB connection.

## Step - 13: code app\core\config.py ## mangodb config file creation

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings


client = AsyncIOMotorClient(settings.mongodb_url)

database = client[settings.mongodb_database]

## Ste -14: Test Configuration:
uv run python -c "from app.core.config import settings; print(settings.mongodb_url); print(settings.mongodb_database)"

job_application_tracker

## step 15: Test the MongoDB client:
uv run python -c "from app.database.mongodb import database; print(database.name)"
job_application_tracker

## step - 16: create the job application schema: 
code app\schemas\application.py

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

## Verify if it imports correctly:
uv run python -c "from app.schemas.application import JobApplicationCreate, ApplicationStatus; print(JobApplicationCreate(company='OpenAI', position='Full Stack AI Developer')); print(ApplicationStatus.APPLIED)"

The output confirms:

JobApplicationCreate was imported successfully.
Required fields company and position were accepted.
Optional fields defaulted to None.
skills defaulted to an empty list.
status correctly defaulted to ApplicationStatus.SAVED.
ApplicationStatus.APPLIED correctly printed as applied.



uv run python -c "from app.schemas.application import JobApplicationCreate, ApplicationStatus; print(JobApplicationCreate(company='OpenAI', position='Full Stack AI Developer')); print(ApplicationStatus.APPLIED)"

## Step-17: Create the MongoDB Repository
code app\repositories\application_repository.py

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

## Verify repository
uv run python -c "from app.repositories.application_repository import COLLECTION_NAME, get_collection; print(COLLECTION_NAME); print(get_collection().name)"

job_applications
job_applications

## Step-18: Check which MongoDB client the project uses

Get-Content app\database\mongodb.py

✅ AsyncIOMotorClient is configured correctly.
✅ It is reading settings.mongodb_url.
✅ It is selecting the job_application_tracker database.
✅ No changes are needed.

## test:
uv run python -c "from app.database.mongodb import database; print(type(database)); print(database.name)"

<class 'motor.motor_asyncio.AsyncIOMotorDatabase'>
job_application_tracker

## Step-19: Commit this completed step

git add app\schemas app\repositories
git commit -m "Add job application schemas and MongoDB repository"
git status

## Step-20: Create the Job Application CRUD API Routes:

## Step-20: Create the routes folder and file

New-Item -ItemType Directory -Path app\api\routes -Force
New-Item -ItemType File -Path app\api\__init__.py -Force
New-Item -ItemType File -Path app\api\routes\__init__.py -Force
code app\api\routes\applications.py

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

## Step-21: Create the main API router

code app\api\router.py

## Ste-22: Connect the API router to FastAPI
code\main.py

from fastapi import FastAPI

app = FastAPI(
    title="Job Application Tracker API",
    description="Full-stack job application tracker using FastAPI and MongoDB",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Job Application Tracker API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/api/v1/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "job-application-tracker",
        "database": "MongoDB",
    }

## step-23: add POST /api/v1/applications.

New-Item -ItemType File -Force app\api\v1\__init__.py
code app\api\v1\applications.py

## step-24: Update: code main.py

from fastapi import FastAPI

from app.api.v1.applications import router as applications_router


app = FastAPI(
    title="Job Application Tracker API",
    description="Full-stack job application tracker using FastAPI and MongoDB",
    version="0.1.0",
)


app.include_router(
    applications_router,
    prefix="/api/v1",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Job Application Tracker API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/api/v1/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "job-application-tracker",
        "database": "MongoDB",
    }

## step-25: ensure FastAPI and Uvicorn are installed:

uv add fastapi "uvicorn[standard]"

## step-24: Start the API:
uv run uvicorn main:app --reload
Uvicorn running on http://127.0.0.1:8000
Application startup complete.

## Open  URLs:
http://127.0.0.1:8000/  
{"message":"Job Application Tracker API","status":"running","docs":"/docs"}
http://127.0.0.1:8000/api/v1/health
{"status":"ok","service":"job-application-tracker","database":"MongoDB"}
http://127.0.0.1:8000/docs

## Step-25: Test the POST request again:

$body = @{
    company         = "Microsoft"
    position        = "AI Software Engineer"
    job_url         = "https://careers.microsoft.com"
    location        = "Redmond, WA"
    work_mode       = "hybrid"
    status          = "applied"
    applied_date    = "2026-07-22"
    salary_range    = '$140,000-$180,000'
    skills          = @(
        "Python"
        "FastAPI"
        "Azure"
        "Docker"
        "AI"
    )
    job_description = "Develop AI-powered enterprise applications."
    notes           = "Applied through Microsoft Careers."
    resume_version  = "Resume-v1"
} | ConvertTo-Json -Depth 5

$response = Invoke-RestMethod `
    -Method Post `
    -Uri "http://127.0.0.1:8000/api/v1/applications" `
    -ContentType "application/json" `
    -Body $body

$response

## Step-26: the application was successfully saved in MongoDB.

The response confirms:

POST /api/v1/applications works.
Pydantic validation works.
MongoDB generated an _id.
Enum fields were stored correctly.
created_at and updated_at were added.
The URL was normalized with a trailing /.

## step-26: verify directly in MongoDB:

mongosh
test> use job_application_tracker
switched to db job_application_tracker

job_application_tracker> db.job_applications.find(
|   { company: "Microsoft" }
| ).pretty()

## View save application:
db.job_applications.find().pretty()

## count them:
db.job_applications.countDocuments()

## test the GET-by-ID method by using returned ID:
ObjectId("6a61066f8be4212c4ca7cd2b")

## step-27: update repository:
code app\repositories\application_repository.py

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


## step-28: Update the API routes
from typing import Any

from fastapi import APIRouter, HTTPException, status

from app.repositories.application_repository import job_application_repository
from app.schemas.application import JobApplicationCreate


router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def create_application(
    application: JobApplicationCreate,
) -> dict[str, Any]:
    try:
        return await job_application_repository.create(application)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create job application.",
        ) from exc


@router.get("")
async def list_applications() -> list[dict[str, Any]]:
    return await job_application_repository.get_all()


@router.get("/{application_id}")
async def get_application(
    application_id: str,
) -> dict[str, Any]:
    application = await job_application_repository.get_by_id(application_id)

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found.",
        )

    return application

## step-29: Test list-all endpoint
Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/api/v1/applications"

## Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/api/v1/applications" |
    ConvertTo-Json -Depth 10

## step-30: Test get-by-ID endpoint:
Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/api/v1/applications/6a61066f8be4212c4ca7cd2b"

## Test 1 – List all applications
Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/api/v1/applications" |
    ConvertTo-Json -Depth 10

## Test 2 – Get one application
Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/api/v1/applications/6a61066f8be4212c4ca7cd2b" |
    ConvertTo-Json -Depth 10

## step-31: Verify directly in MongoDB Shell:

mongosh "mongodb://localhost:27017/job_application_tracker"
job_application_tracker> show collections
applications
job_applications
system_check
job_application_tracker> db.job_applications.find().pretty()
[
  {
    _id: ObjectId('6a61066f8be4212c4ca7cd2b'),
    company: 'Microsoft',
    position: 'AI Software Engineer',
    job_url: 'https://careers.microsoft.com/',
    location: 'Redmond, WA',
    work_mode: 'hybrid',
    status: 'applied',
    applied_date: '2026-07-22',
    salary_range: '$140,000-$180,000',
    skills: [ 'Python', 'FastAPI', 'Azure', 'Docker', 'AI' ],
    job_description: 'Develop AI-powered enterprise applications.',
    notes: 'Applied through Microsoft Careers.',
    resume_version: 'Resume-v1',
    created_at: ISODate('2026-07-22T18:05:35.707Z'),
    updated_at: ISODate('2026-07-22T18:05:35.707Z')
  }
]
job_application_tracker> exit

## step-32: Commit the CRUD API
git add .
git commit -m "Add CRUD API for job applications using FastAPI and MongoDB"
git push origin main

## step-33: Delete 

## unused files
Remove-Item app\api\router.py
Remove-Item -Recurse -Force app\api\routes

## Delete Python cache folders
Get-ChildItem app -Recurse -Directory -Filter "__pycache__" |
    Remove-Item -Recurse -Force

## Verify the structure:
tree app /F

## step-34: Add Safe CRUD API Tests:

## Confirm testing packages
uv add --dev pytest pytest-asyncio httpx
uv sync

## erify:
uv run pytest --version
pytest 9.1.1

## Create: code tests\conftest.py
from collections.abc import AsyncIterator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from pymongo import AsyncMongoClient

import app.repositories.application_repository as application_repository
from app.core.config import settings
from main import app


TEST_DATABASE_NAME = "job_application_tracker_test"


@pytest_asyncio.fixture
async def test_database(
    monkeypatch,
) -> AsyncIterator[None]:
    """
    Connect the repository to a separate MongoDB test database.

    The real job_application_tracker database is never changed.
    """
    client = AsyncMongoClient(settings.mongodb_url)
    test_database = client[TEST_DATABASE_NAME]

    monkeypatch.setattr(
        application_repository,
        "database",
        test_database,
    )

    await test_database.drop_collection(
        application_repository.COLLECTION_NAME
    )

    yield

    await test_database.drop_collection(
        application_repository.COLLECTION_NAME
    )

    await client.close()


@pytest_asyncio.fixture
async def client(
    test_database,
) -> AsyncIterator[AsyncClient]:
    del test_database

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as async_client:
        yield async_client

## step-35: Create the CRUD tests
code tests\test_applications.py

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

## tree tests /F



## Step-36: main.py
from fastapi import FastAPI

from app.api.router import api_router


app = FastAPI(
    title="AI Job Application Tracker",
    description=(
        "Full Stack Generative AI and Agentic AI "
        "Job Application Tracking Platform"
    ),
    version="0.1.0",
)


app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    return {
        "message": "AI Job Application Tracker API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/api/v1/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "AI Job Application Tracker",
        "database": "job_application_tracker",
    }

## New-Item -ItemType Directory -Path app\api\routes -Force | Out-Null
## New-Item -ItemType File -Path app\api\__init__.py -Force | Out-Null
## New-Item -ItemType File -Path app\api\routes\__init__.py -Force | Out-Null
## code app\api\router.py

from fastapi import APIRouter

from app.api.routes.applications import router as applications_router


api_router = APIRouter()
api_router.include_router(applications_router)

## New-Item -ItemType File -Path app\api\routes\applications.py -Force

code app\api\routes\applications.py

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
    created = await create_application(application)
    return JobApplicationResponse.model_validate(created)


@router.get(
    "",
    response_model=list[JobApplicationResponse],
)
async def get_job_applications(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[JobApplicationResponse]:
    applications = await list_applications(skip=skip, limit=limit)

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
    updated = await update_application(
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
    deleted = await delete_application(application_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)

## Verify
Test-Path app\api\routes\applications.py

## verify whether the main router exists:
Test-Path app\api\router.py
True

## Test
uv run python -c "from main import app; print(app.title)"

## step-37: Update the repository class
code app\repositories\application_repository.py

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

## step-37: Update the route file
code app\api\routes\applications.py

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

## step-38: Verify the imports
uv run python -c "from app.repositories.application_repository import job_application_repository; print(type(job_application_repository).__name__)"
print(type(job_application_repository).__name__)"

JobApplicationRepository

## step-39: uv run python -c "from main import app; print(app.title)"
AI Job Application Tracker

## step-40: Test
uv run pytest tests\test_applications.py -v

## Update: code tests\conftest.py

from collections.abc import AsyncIterator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from pymongo import AsyncMongoClient

from app.core.config import settings
from app.repositories.application_repository import (
    job_application_repository,
)
from main import app


TEST_DATABASE_NAME = "job_application_tracker_test"
TEST_COLLECTION_NAME = "job_applications"


@pytest_asyncio.fixture
async def test_database(
    monkeypatch,
) -> AsyncIterator[None]:
    """
    Connect the repository to a separate MongoDB test database.

    The real job_application_tracker database is never changed.
    """
    client = AsyncMongoClient(settings.mongodb_url)
    test_database = client[TEST_DATABASE_NAME]
    test_collection = test_database[TEST_COLLECTION_NAME]

    monkeypatch.setattr(
        job_application_repository,
        "collection",
        test_collection,
    )

    await test_database.drop_collection(TEST_COLLECTION_NAME)

    yield

    await test_database.drop_collection(TEST_COLLECTION_NAME)
    await client.close()


@pytest_asyncio.fixture
async def client(
    test_database,
) -> AsyncIterator[AsyncClient]:
    del test_database

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as async_client:
        yield async_client

## Run
uv run pytest tests\test_applications.py -v
7 passed in 0.27s

## save in git

## git add .
## git commit -m "Add tested CRUD API for job applications"
## git push origin main

## Milestone completed ✅

You now have:

✅ FastAPI application
✅ MongoDB integration
✅ Repository layer
✅ Pydantic schemas
✅ CRUD REST API
✅ Automated pytest suite (7/7 passing)
✅ Separate MongoDB test database
✅ Git commit ready

## step-40: AI-powered Resume Matching.

Job Description
        │
        ▼
FastAPI Endpoint
        │
        ▼
Resume Parser
        │
        ▼
OpenAI GPT
        │
        ▼
JSON Analysis
        │
        ├── Match Score
        ├── Missing Skills
        ├── Strengths
        ├── Weaknesses
        └── Resume Suggestions
        │
        ▼
MongoDB

## Install dependencies:
uv add openai python-dotenv pypdf python-docx
uv sync

## Verify:
uv run python -c "import openai,pypdf,docx;print('Packages installed successfully')"

Packages installed successfull

## Create the AI folder

mkdir app\ai
New-Item app\ai\__init__.py -ItemType File
code app\ai\resume_matcher.py

from pathlib import Path

from docx import Document
from pypdf import PdfReader


SUPPORTED_RESUME_EXTENSIONS = {".pdf", ".docx", ".txt"}


def extract_text_from_pdf(file_path: Path) -> str:
    """Extract readable text from a PDF resume."""
    reader = PdfReader(str(file_path))

    pages: list[str] = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages.append(page_text.strip())

    return "\n\n".join(pages).strip()


def extract_text_from_docx(file_path: Path) -> str:
    """Extract text from paragraphs and tables in a DOCX resume."""
    document = Document(str(file_path))

    sections: list[str] = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            sections.append(text)

    for table in document.tables:
        for row in table.rows:
            values = [
                cell.text.strip()
                for cell in row.cells
                if cell.text.strip()
            ]

            if values:
                sections.append(" | ".join(values))

    return "\n".join(sections).strip()


def extract_text_from_txt(file_path: Path) -> str:
    """Read text from a plain-text resume."""
    return file_path.read_text(
        encoding="utf-8",
        errors="ignore",
    ).strip()


def extract_resume_text(file_path: str | Path) -> str:
    """
    Extract resume text from PDF, DOCX, or TXT.

    Raises:
        FileNotFoundError: When the resume file does not exist.
        ValueError: When the file type is unsupported or contains no text.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Resume file was not found: {path}"
        )

    extension = path.suffix.lower()

    if extension not in SUPPORTED_RESUME_EXTENSIONS:
        supported = ", ".join(
            sorted(SUPPORTED_RESUME_EXTENSIONS)
        )

        raise ValueError(
            f"Unsupported resume format: {extension}. "
            f"Supported formats: {supported}"
        )

    if extension == ".pdf":
        text = extract_text_from_pdf(path)
    elif extension == ".docx":
        text = extract_text_from_docx(path)
    else:
        text = extract_text_from_txt(path)

    if not text:
        raise ValueError(
            "No readable text was found in the resume."
        )

    return text

## .env
OPENAI_API_KEY=your_openai_api_key_here

## uv run python -c "import openai,pypdf,docx;print('Packages installed successfully')"
Packages installed successfully

## Verify:
Test-Path app\ai\resume_matcher.py
True

## verify parser imports 
uv run python -c "from app.ai.resume_matcher import extract_resume_text; print('Resume parser imported successfully')"
Resume parser imported successfully

## Test with a temporary text resume
@"
Mamatha Pinnamaneni
Full Stack AI Developer

Skills:
Python, FastAPI, MongoDB, Docker, Generative AI
"@ | Set-Content test_resume.txt

## uv run python -c "from app.ai.resume_matcher import extract_resume_text; print(extract_resume_text('test_resume.txt'))"

## Remove-Item test_resume.txt
Remove-Item test_resume.txt

## verify:
Test-Path test_resume.txt

## create add the AI analysis schema:
code app\schemas\resume_analysis.py

from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):
    match_score: int = Field(ge=0, le=100)
    matching_skills: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    summary: str

## verify
uv run python -c "from app.schemas.resume_analysis import ResumeAnalysis; print(ResumeAnalysis.model_fields.keys())"

dict_keys(['match_score', 'matching_skills', 'missing_skills', 'strengths', 'weaknesses', 'recommendations', 'summary'])

## step-41: create the AI resume-matching service:
code app\ai\resume_matcher.py

## code app\services\resume_parser.py

from pathlib import Path

from docx import Document
from pypdf import PdfReader


SUPPORTED_RESUME_EXTENSIONS = {".pdf", ".docx", ".txt"}


def extract_text_from_pdf(file_path: Path) -> str:
    """Extract readable text from a PDF resume."""
    reader = PdfReader(str(file_path))
    pages: list[str] = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages.append(page_text.strip())

    return "\n\n".join(pages).strip()


def extract_text_from_docx(file_path: Path) -> str:
    """Extract text from paragraphs and tables in a DOCX resume."""
    document = Document(str(file_path))
    sections: list[str] = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            sections.append(text)

    for table in document.tables:
        for row in table.rows:
            values = [
                cell.text.strip()
                for cell in row.cells
                if cell.text.strip()
            ]

            if values:
                sections.append(" | ".join(values))

    return "\n".join(sections).strip()


def extract_text_from_txt(file_path: Path) -> str:
    """Read text from a plain-text resume."""
    return file_path.read_text(
        encoding="utf-8",
        errors="ignore",
    ).strip()


def extract_resume_text(file_path: str | Path) -> str:
    """
    Extract resume text from PDF, DOCX, or TXT.

    Raises:
        FileNotFoundError: When the resume does not exist.
        ValueError: When the format is unsupported or contains no text.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Resume file was not found: {path}"
        )

    if not path.is_file():
        raise ValueError(
            f"Resume path is not a file: {path}"
        )

    extension = path.suffix.lower()

    if extension not in SUPPORTED_RESUME_EXTENSIONS:
        supported = ", ".join(
            sorted(SUPPORTED_RESUME_EXTENSIONS)
        )

        raise ValueError(
            f"Unsupported resume format: {extension}. "
            f"Supported formats: {supported}"
        )

    if extension == ".pdf":
        text = extract_text_from_pdf(path)
    elif extension == ".docx":
        text = extract_text_from_docx(path)
    else:
        text = extract_text_from_txt(path)

    if not text:
        raise ValueError(
            "No readable text was found in the resume."
        )

    return text

## code app\services\resume_analysis_service.py

import os

from dotenv import load_dotenv
from openai import OpenAI

from app.schemas.resume_analysis import ResumeAnalysis


load_dotenv()


def get_openai_client() -> OpenAI:
    """Create an OpenAI client using the environment API key."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Add it to the .env file."
        )

    return OpenAI(api_key=api_key)


def analyze_resume_match(
    resume_text: str,
    job_description: str,
) -> ResumeAnalysis:
    """Compare resume text with a job description using AI."""
    cleaned_resume = resume_text.strip()
    cleaned_job_description = job_description.strip()

    if not cleaned_resume:
        raise ValueError("Resume text cannot be empty.")

    if not cleaned_job_description:
        raise ValueError("Job description cannot be empty.")

    client = get_openai_client()

    response = client.responses.parse(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are an expert technical recruiter and ATS resume "
                    "analyst. Compare the candidate's resume with the job "
                    "description. Be accurate and do not invent experience."
                ),
            },
            {
                "role": "user",
                "content": (
                    "RESUME:\n"
                    f"{cleaned_resume}\n\n"
                    "JOB DESCRIPTION:\n"
                    f"{cleaned_job_description}"
                ),
            },
        ],
        text_format=ResumeAnalysis,
    )

    analysis = response.output_parsed

    if analysis is None:
        raise RuntimeError(
            "The AI response could not be parsed."
        )

    return analysis

## Verify imports
uv run python -c "from app.services.resume_parser import extract_resume_text; from app.services.resume_analysis_service import analyze_resume_match; print('Resume services imported successfully')"
Resume services imported successfully

## Step-42: Create the resume analysis API endpoint:

## Create the request schema
code app\schemas\resume_request.py

from pydantic import BaseModel, Field


class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(
        min_length=1,
        description="Extracted resume text.",
    )
    job_description: str = Field(
        min_length=1,
        description="Job description to compare with the resume.",
    )

## Step-43: Create the resume analysis route

code app\api\v1\resume_analysis.py

from fastapi import APIRouter, HTTPException, status
from openai import OpenAIError

from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.resume_request import ResumeAnalysisRequest
from app.services.resume_analysis_service import analyze_resume_match


router = APIRouter(
    prefix="/resume-analysis",
    tags=["Resume Analysis"],
)


@router.post(
    "",
    response_model=ResumeAnalysis,
    status_code=status.HTTP_200_OK,
)
def analyze_resume(
    request: ResumeAnalysisRequest,
) -> ResumeAnalysis:
    """Compare resume text with a job description."""
    try:
        return analyze_resume_match(
            resume_text=request.resume_text,
            job_description=request.job_description,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except OpenAIError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The AI service could not complete the analysis.",
        ) from exc
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc

## Add router: code main.py


from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="AI Job Application Tracker",
    description=(
        "Full Stack Generative AI and Agentic AI "
        "Job Application Tracking Platform"
    ),
    version="0.1.0",
)

# Register all API routes
app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to the AI Job Application Tracker API",
        "status": "running",
        "version": "0.1.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


@app.get("/api/v1/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "AI Job Application Tracker",
        "database": "job_application_tracker",
    }

## Verify
uv run uvicorn main:app --reload

## Test the Root Endpoint
Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/"

message  : Welcome to the AI Job Application Tracker API
status   : running
version  : 0.1.0
docs     : /docs
openapi  : /openapi.json

## Test the Health Endpoint
Invoke-RestMethod `
    -Method Get `
    -Uri "http://127.0.0.1:8000/api/v1/health"

status    : ok
service   : AI Job Application Tracker
database  : job_application_tracker

## step-44: AI Resume Analysis API

## Create a new route:
mkdir app\api\routes\resume
New-Item app\api\routes\resume\__init__.py -ItemType File
code app\api\routes\resume.py

from fastapi import APIRouter

router = APIRouter(
    prefix="/resume",
    tags=["Resume AI"],
)


@router.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "Resume AI",
    }

## update app/api/router.py to include the new router:
code app/api/router.py

from fastapi import APIRouter

from app.api.routes.applications import router as applications_router
from app.api.routes.resume import router as resume_router

api_router = APIRouter()

api_router.include_router(applications_router)
api_router.include_router(resume_router)

## Restart your FastAPI server and open:
uv run uvicorn main:app --reload

## delete the duplicate resume folder
Remove-Item -Recurse -Force app\api\routes\resume
## tree app\api\routes /F

## run: Get-Content app\api\routes\resume.py


## Step-45: Implement the AI Resume Analysis Endpoint:

## Create the request model

## code app/schemas/resume_request.py

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

## Update app/api/routes/resume.py

from fastapi import APIRouter, HTTPException

from app.ai.resume_matcher import (
    analyze_resume_match,
    extract_resume_text,
)
from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.resume_request import ResumeAnalysisRequest

router = APIRouter(
    prefix="/resume",
    tags=["Resume AI"],
)


@router.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "Resume AI",
    }


@router.post(
    "/analyze",
    response_model=ResumeAnalysis,
)
async def analyze_resume(
    request: ResumeAnalysisRequest,
) -> ResumeAnalysis:
    try:
        resume_text = extract_resume_text(
            request.resume_path
        )

        return analyze_resume_match(
            resume_text=resume_text,
            job_description=request.job_description,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

## Restart FastAPI

## Step-44: End-to-End AI Test

## create sample_resume.txt

Anita Kotha
anita.kotha@Gmail.com

________________________________________
PROFESSIONAL SUMMARY
Foreign Medical Graduate with extensive healthcare and health IT experience, specializing in Electronic Health Record (EHR) implementation, Epic deployment, clinical workflow optimization, and healthcare transformation initiatives. Experienced in collaborating with physicians, nurses, clinical leadership, and technical teams to implement and support Epic applications across hospital and ambulatory care settings. Strong understanding of clinical operations, patient care workflows, healthcare regulations, and interoperability standards. Proven ability to bridge the gap between clinical and technical stakeholders, drive user adoption, support go-live activities, and deliver successful EHR implementations that improve operational efficiency, documentation quality, and patient outcomes.
PROFESSIONAL EXPERIENCE
Release and Deployment Consultant iV
Kaiser Permanente California
January 2006 – May 2026
•	Collaborated with physicians, CDI specialists, HIM teams, and IT staff to improve documentation quality and coding accuracy.
•	Supported Epic EHR optimization projects, resulting in a 20% reduction in documentation deficiencies.
•	Designed and implemented documentation workflows aligned with regulatory and reimbursement requirements.
•	Facilitated HL7 interface testing and validation between EHR, laboratory, and radiology systems.
•	Conducted user training sessions for providers and clinical staff regarding documentation best practices.
•	Served as a liaison between business stakeholders and Epic technical teams, ensuring code changes and system enhancements were thoroughly validated and approved before production deployment. 
•	 Led end-to-end validation of Epic build and configuration changes, coordinating testing, defect resolution, and release activities to support successful production implementations with minimal post-go-live issues. 
•	 Managed release validation processes for Epic applications, ensuring compliance with change control procedures and maintaining system stability across multiple environments.
Kaiser Permanente, California
Release and Deployment Consultant III
June 2016 – December 2019
•	Participated in enterprise-wide EHR implementation and integration projects.
•	Gathered business and clinical requirements from stakeholders across multiple departments.
•	Created workflow diagrams and functional specifications for clinical documentation enhancements.
•	Assisted in FHIR and HL7 data mapping activities for external healthcare systems.
•	Supported testing, issue resolution, and go-live activities.
•	Improved provider adoption through training and workflow optimization initiatives.

Business Consultant Lead
Kaiser Permanente, California
August 2012 – May 2016
•	Reviewed clinical documentation for completeness, accuracy, and compliance.
•	Worked with physicians to clarify diagnoses and documentation gaps.
•	Supported ICD-10 transition efforts and coding quality initiatives.
•	Maintained documentation compliance with CMS and Joint Commission standards.
Business Consultant Senior
May 2006- May 2016
•	Led Epic deployment activities for a multi-hospital healthcare system serving 10,000+ providers and 5M+ patients. 
•	Directed cross-functional teams through planning, testing, training, cutover, and go-live phases of Epic implementation. 
•	Managed deployment schedules, risk mitigation strategies, and stakeholder communications for enterprise EHR transformation initiatives. 
•	Oversaw command center operations during go-live, achieving 98% issue resolution within established service-level agreements. 
•	Improved provider adoption rates by implementing targeted training and workflow optimization programs. 
•	Coordinated enterprise data conversion and integration efforts involving 100+ interfaces and legacy clinical applications.
Voluntary experience
Millcreek community Hospital , Erie PA
Completed a 12-month rotating internship, where I took patient histories, reviewed lab results, diagnosed conditions, and prescribed medications under physician supervision.

________________________________________
EDUCATION
Bachelor of Medicine and Bachelor of Surgery ( M.B.B.S)
Dr BM Patil’s BLDE A’s Medical College
MBA (Business Administration)
University of Phoenix- California

________________________________________



TECHNICAL SKILLS
EHR Platforms
•	Epic
•	Citrix

Healthcare Standards
•	HL7 v2/v3
•	FHIR
•	ICD-10-CM
•	CPT
Tools
•	Microsoft office 
•	Microsoft Excel
•	Power BI
•	Share point
•	ServiceNow
•	UI Path Automation






## step-45:

