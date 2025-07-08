import re

def extract_skills_from_job(job_text):
    skills = re.findall(r'\b(Java|Python|Flutter|SQL|Django|HTML|CSS|React|ML|AI|NodeJS|Kotlin|MongoDB)\b', job_text, re.IGNORECASE)
    return list(set([s.capitalize() for s in skills]))
