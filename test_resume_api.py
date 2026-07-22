from pathlib import Path

import httpx

API_URL = "http://127.0.0.1:8000/api/v1/resume/analyze"

resume_text = Path("sample_resume.txt").read_text(encoding="utf-8")
job_description = Path("sample_job_description.txt").read_text(
    encoding="utf-8"
)

payload = {
    "resume_text": resume_text,
    "job_description": job_description,
}

try:
    response = httpx.post(
        API_URL,
        json=payload,
        timeout=120.0,
    )
    response.raise_for_status()
except httpx.HTTPError as exc:
    print(f"API request failed: {exc}")
else:
    result = response.json()

    print(f"Match score: {result['match_score']}%")
    print("\nMatching skills:")
    for skill in result["matching_skills"]:
        print(f"- {skill}")

    print("\nMissing skills:")
    for skill in result["missing_skills"]:
        print(f"- {skill}")

    print("\nRecommendations:")
    for recommendation in result["recommendations"]:
        print(f"- {recommendation}")

    print("\nSummary:")
    print(result["summary"])