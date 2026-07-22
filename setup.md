## Job-Application-Tracker-with-MongoDB

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

##*********************************************************************************                               Phase 1 — Verify MongoDB
##*********************************************************************************

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

##*********************************************************************************                               ## connect your git, github
##*********************************************************************************

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



Create github project:    
job-application-tracker-with-mongodb









