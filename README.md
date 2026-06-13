# 🤖 AI Job Matcher

An AI-powered job recommendation platform that matches a user's resume with relevant job opportunities and provides personalized job recommendations based on skills, experience, and job requirements.

## 🚀 Features

* 📄 Upload Resume (PDF)
* 🔍 Automatic Resume Text Extraction
* 💼 Fetch Latest Job Listings
* 🤖 AI-Based Resume and Job Matching
* 📊 Match Score Calculation
* 🎯 Fresher Suitability Detection
* 🛠 Missing Skills Identification
* 📈 Job Level Classification
* 🔗 Direct Apply Links for Jobs

---

## 🏗️ Project Architecture

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
Extract Resume Text
      │
      ▼
Job Scraper
      │
      ▼
Fetch Job Listings
      │
      ▼
AI Matching Engine
      │
      ▼
Score Calculation
      │
      ▼
Top Job Recommendations
```

---

## 📂 Project Structure

```text
job-ai-platform/
│
├── app.py
│
├── ai/
│   └── matcher.py
│
├── scraper/
│   └── scraper.py
│
├── utils/
│   ├── resume_parser.py
│   └── cache.py
│
├── database/
│   └── db.py
│
├── requirements.txt
├── cache.json
└── README.md
```

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Libraries

* Pandas
* Streamlit
* PDF Processing Libraries
* Requests
* BeautifulSoup (for scraping)

### AI & NLP

* Custom Resume Matching Logic
* Skill Gap Analysis

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KoppoluManeesha/job-ai-platform.git
cd job-ai-platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Upload your resume in PDF format.
2. The system extracts text from the resume.
3. Job listings are collected through the scraper.
4. The AI matching engine compares your skills with job requirements.
5. A matching score is generated for each job.
6. Missing skills and suitability information are displayed.
7. The best matching jobs are ranked and shown to the user.

---

## 📊 Example Output

### Python Developer

**Company:** ABC Technologies

**Location:** Hyderabad

**Match Score:** 92%

**Level:** Entry Level

**Fresher Suitable:** Yes

**Missing Skills:** Docker, AWS

**Reason:** Strong match in Python, Django, REST APIs, and SQL.

---

## 🔮 Future Enhancements

* User Authentication
* Save Favorite Jobs
* AI Career Guidance
* Resume Improvement Suggestions
* Job Alerts
* Multi-Platform Job Aggregation
* Dashboard Analytics

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 👨‍💻 Author

**Maneesha Koppolu**

GitHub: https://github.com/KoppoluManeesha

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
