from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

# ================================
# Job Role Skill Set (Data Analyst)
# ================================
JOB_SKILLS = {
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "statistics",
    "data analysis",
    "pandas",
    "numpy",
    "visualization"
}

# ================================
# Skill Improvement Recommendations
# ================================
SKILL_RESOURCES = {
    "pandas": "Learn Pandas for data manipulation and data cleaning",
    "numpy": "Practice NumPy for numerical and matrix operations",
    "statistics": "Strengthen statistics concepts like mean, variance, probability",
    "data analysis": "Work on real-world data analysis projects using datasets"
}

# ================================
# Routes
# ================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["resume"]

    # -------- PDF Text Extraction --------
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    text_lower = text.lower()

    # -------- Skill Extraction --------
    resume_skills = set()
    for skill in JOB_SKILLS:
        if skill in text_lower:
            resume_skills.add(skill)

    # -------- Skill Comparison --------
    matched_skills = resume_skills
    missing_skills = JOB_SKILLS - resume_skills

    # -------- Score Calculation --------
    score = int((len(matched_skills) / len(JOB_SKILLS)) * 100)

    # -------- Recommendations --------
    recommendations = []
    for skill in missing_skills:
        if skill in SKILL_RESOURCES:
            recommendations.append(SKILL_RESOURCES[skill])

    return render_template(
        "result.html",
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        recommendations=recommendations
    )

# ================================
# App Runner
# ================================
if __name__ == "__main__":
    app.run(debug=True)
