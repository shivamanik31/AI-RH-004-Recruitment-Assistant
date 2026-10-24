# AI Recruitment Assistant

**Project Code:** AI-RH-004  
**Student Code:** DAS011046

## 1. Project Overview

The AI Recruitment Assistant is a Python-based web application designed to simplify and support recruitment activities. It helps recruiters analyze job descriptions, extract skills from candidate resumes, calculate candidate matching scores, rank candidates, prepare interview details, and generate recruitment email drafts.

The application provides a simple, interactive interface built using Streamlit.

## 2. Objectives

- Identify relevant skills from resume text.
- Analyze job descriptions to identify required skills.
- Compare candidate skills against job requirements.
- Calculate matching scores and rank candidates.
- Support candidate shortlisting.
- Prepare interview scheduling details.
- Generate downloadable recruitment email drafts.
- Export candidate matching and shortlisting results as CSV files.

## 3. Features

### Resume and Job Description Analysis
Extracts supported technical and professional skills from resume text and job descriptions using keyword matching.

### Candidate Matching
Calculates a candidate match percentage based on the overlap between extracted candidate skills and required job skills.

### Candidate Ranking and Shortlisting
Ranks candidates according to their matching scores and allows recruiters to set a minimum score for shortlisting.

### Interview Scheduler
Collects interview information, including candidate name, date, time, interviewer, interview type, and meeting location or link.

### Email Draft Generator
Creates recruitment email drafts for interview invitations, shortlist notifications, and application updates.

### Data Export
Allows users to download candidate matching results and shortlist information as CSV files, and email drafts as text files.

### Recruitment Dashboard
Displays candidate information, required skills, and basic recruitment statistics.

## 4. Technologies Used

- **Python** — Application programming language
- **Streamlit** — Interactive web application interface
- **Pandas** — Candidate data management and analysis
- **Scikit-learn** — Machine learning utilities included in the project dependencies
- **NLTK** — Natural language processing library included in the project dependencies

## 5. Project Structure

```text
AI Recruitment Assistant (AI-RH-004)/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .venv/
└── screenshots/
    ├── 01_dashboard.png
    ├── 02_job_matching.png
    ├── 03_shortlisting.png
    ├── 04_interview_scheduler.png
    ├── 05_email_draft.png
    └── 06_project_files.png
```

The `screenshots` folder should contain screenshots you capture from your actual application. The `.venv` folder is a local virtual environment and should not be uploaded to GitHub.

## 6. Installation and Setup

### Prerequisites
- Python installed on your computer
- Visual Studio Code or another Python editor
- Git, if you want to upload the project to GitHub

### Step 1: Open the project folder

Open the project folder in your terminal.

### Step 2: Install the dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the application

Start the web application using:

```bash
python -m streamlit run app.py
```

Alternatively, run the launcher:

```bash
python main.py
```

### Step 4: Open the application

Streamlit will display a local URL in the terminal, usually:

`http://localhost:8501`

Open this URL in your web browser.

## 7. How to Use

1. Open the Recruitment Dashboard to view the sample candidate data.
2. Navigate to Resume & Job Matching to analyze a job description and add candidate resume text.
3. Review extracted skills and candidate matching scores.
4. Open Candidate Shortlisting to set a minimum match-score threshold.
5. Use Interview Scheduler to prepare interview details.
6. Use Email Draft Generator to create and download recruitment email drafts.
7. Download matching results or shortlist data in CSV format.

## 8. Limitations

- Skill extraction uses a predefined keyword list.
- Candidate matching is based on skill overlap and is not a trained recruitment prediction model.
- The application starts with sample candidate data for demonstration.
- Resume text must be pasted into the application; automatic PDF or DOCX resume parsing is not implemented in this version.
- Interview details are prepared within the application; calendar events and invitations are not created automatically.
- Email drafts can be downloaded, but emails are not sent automatically.
- Recruitment decisions require human review. Match scores should not be treated as definitive measures of a candidate's suitability.

## 9. Future Enhancements

- Support uploading and parsing PDF and DOCX resumes.
- Improve skill extraction using NLP techniques.
- Add a persistent database for candidate records.
- Integrate calendar services for interview scheduling.
- Integrate email services for authorized email delivery.
- Add more recruitment analytics and reporting.
- Evaluate matching accuracy using a representative, appropriately labeled dataset.

## 10. Conclusion

The AI Recruitment Assistant demonstrates how a Python-based web application can support several recruitment workflows, including skill extraction, candidate matching, ranking, interview planning, and email draft generation.

The project provides a foundation for future improvements in recruitment automation and data-driven candidate management.

---

**Project:** AI Recruitment Assistant  
**Project Code:** AI-RH-004  
**Student Code:** DAS011046