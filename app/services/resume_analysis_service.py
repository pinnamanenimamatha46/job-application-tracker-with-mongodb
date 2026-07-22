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