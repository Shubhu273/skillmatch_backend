from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_parser import extract_skills_from_resume
from job_parser import extract_skills_from_job
from course_recommender import get_courses_for_skill
import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files['resume']
    job_desc = request.form['job_desc']

    resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(resume_path)

    resume_skills = extract_skills_from_resume(resume_path)
    job_skills = extract_skills_from_job(job_desc)
    missing_skills = [s for s in job_skills if s not in resume_skills]

    courses = {}
    for skill in missing_skills:
        courses[skill] = get_courses_for_skill(skill)

    return jsonify({
        'resume_skills': resume_skills,
        'job_skills': job_skills,
        'missing_skills': missing_skills,
        'course_recommendations': courses
    })

if __name__ == '__main__':
    app.run(debug=True)
