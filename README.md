# AI Resume Analyzer 🧠📄

An AI-powered web application that analyzes resumes, evaluates job-role compatibility, and provides actionable skill improvement recommendations — presented through a premium, executive-style dashboard UI.

---

## 🚀 Features

- Upload resume in **PDF format**
- Extracts resume text automatically
- Matches skills against a **Data Analyst role**
- Generates a **Role Compatibility Score**
- Highlights:
  - ✅ Matching skills
  - ❌ Skill gaps
- Provides **personalized recommendations**
- Premium **dark blue × gold dashboard UI**

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Resume Parsing:** PyPDF2
- **Frontend:** HTML, CSS, Bootstrap 5
- **UI Design:** Custom dark-theme dashboard

---

## 📊 Dashboard Preview

![Resume Analyzer Dashboard](screenshots/dashboard.png)

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. Resume text is extracted using PyPDF2
3. Skills are detected via keyword matching
4. Resume is compared against job-role requirements
5. A compatibility score is calculated
6. Skill gaps and improvement suggestions are displayed

---

## 🧪 Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git

# Move into project directory
cd AI-Resume-Analyzer

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

Visit:
👉 http://127.0.0.1:5000

🎯 Use Cases

Resume self-evaluation

Career gap analysis

Internship / job preparation

Portfolio demonstration project

📌 Future Enhancements

Multiple job role selection

ATS-style weighted scoring

Resume PDF export

Dark/Light theme toggle

Cloud deployment

👤 Author

Aarya Khaire
AI & Data Science Enthusiast