# 🎯 AI Study Plan Generator

An AI-powered personalized study planner designed for competitive exam aspirants such as **UPSC, NEET, JEE, GATE, SSC, and CAT**.  
The system dynamically generates **day-wise study plans**, adapts to user performance, prevents burnout, and ensures disciplined preparation.

---

## 🚀 Features

- 📅 **Personalized Day-wise Study Plan**
- 📊 **Subject-wise Strength & Weakness Analysis**
- 🔁 **Adaptive Planning using Reinforcement Learning concepts**
- 🧠 **Clustering-based Student Profiling**
- ✅ **Task-level Checklist (Concept & Practice tracked separately)**
- 🔄 **Automatic Carry-forward of Incomplete Tasks**
- 🧪 **Weekly Revision & Mock Test Scheduling**
- 😌 **Burnout Control with Rest Days (Every 15 Days)**
- 📝 **User-defined Mock Test Count & Question Targets**
- 🌐 **Interactive Streamlit Dashboard**

---

## 🧠 How It Works (High-Level)

1. User selects:
   - Competitive exam
   - Total preparation days
   - Daily study hours
   - Subject-wise confidence level
2. System:
   - Allocates days using weighted logic
   - Rotates topics & subtopics intelligently
   - Inserts revision days, mock tests, and rest days
3. User marks tasks as completed
4. Incomplete tasks are automatically carried forward
5. Reinforcement logic adapts future tasks based on performance

---

## 🏗️ Project Architecture

AI-Study-Plan-Generator/
│
├── app.py # Streamlit frontend
├── planner_engine.py # Core planning logic
├── reinforcement.py # Adaptive learning logic
├── clustering.py # Student profiling
├── utils/
│ └── scheduler.py # Revision & mock scheduler
│
├── syllabus/
│ ├── upsc.json
│ ├── neet.json
│ ├── jee.json
│ ├── gate.json
│ ├── ssc.json
│ └── cat.json
│
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit** – Interactive UI
- **Pandas / NumPy** – Data handling
- **Scikit-learn** – Clustering & ML logic
- **Reinforcement Learning Concepts**
- **JSON-based syllabus management**

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/ai-study-plan-generator.git
cd ai-study-plan-generator
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the App
bash
Copy code
streamlit run app.py
🌐 Deployment
The application can be deployed easily using Streamlit Cloud:

Push code to GitHub

Connect repository on Streamlit Cloud

Select app.py as entry point

Deploy 🚀

🎯 Use Cases
Competitive exam aspirants (UPSC, NEET, JEE, GATE, SSC, CAT)

Personalized self-study planning

Burnout-aware long-term preparation

Adaptive learning & progress tracking



👨‍💻 Author
Krishnanshu Jaiswal
Aspiring Data Scientist | Machine Learning Enthusiast

🔗 LinkedIn: https://www.linkedin.com/in/krishnanshu-jaiswal-70467424b/
🔗 GitHub: https://github.com/Krishnanshuj

⭐ If you like this project
Don’t forget to star ⭐ the repository and share feedback!
