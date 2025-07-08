from pdfminer.high_level import extract_text
import re

def extract_skills_from_resume(pdf_path):
    text = extract_text(pdf_path)
    skills = re.findall(r'\b(Java|Python|Flutter|SQL|Django|HTML|CSS|React|ML|AI|NodeJS|Kotlin|MongoDB)\b', text, re.IGNORECASE)
    return list(set([s.capitalize() for s in skills]))
