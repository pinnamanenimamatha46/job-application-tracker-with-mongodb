from pathlib import Path

from app.ai.resume_matcher import analyze_resume_match

resume_text = Path("sample_resume.txt").read_text(encoding="utf-8")
job_description = Path("sample_job_description.txt").read_text(encoding="utf-8")

result = analyze_resume_match(
    resume_text=resume_text,
    job_description=job_description,
)

print(result)