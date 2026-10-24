
import re
from datetime import date, time

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

st.set_page_config(
    page_title="AI Recruitment Assistant",
    page_icon="👥",
    layout="wide"
)

SKILLS = [
    "python", "java", "sql", "excel", "pandas", "numpy",
    "machine learning", "deep learning", "data science",
    "artificial intelligence", "html", "css", "javascript",
    "react", "streamlit", "power bi", "tableau", "aws",
    "communication", "leadership", "git", "scikit-learn",
    "nlp", "statistics", "data analysis", "tensorflow"
]

def extract_skills(text):
    text = text.lower()
    return sorted({
        skill for skill in SKILLS
        if re.search(r"(?<!\w)" + re.escape(skill) + r"(?!\w)", text)
    })

def calculate_match(candidate_skills, job_skills):
    if not job_skills:
        return 0.0
    matched = set(candidate_skills) & set(job_skills)
    return round(len(matched) / len(set(job_skills)) * 100, 2)

st.title("👥 AI Recruitment Assistant")
st.caption("Resume skill extraction • Job matching • Candidate ranking • Interview planning")

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Choose a module",
        [
            "Dashboard",
            "Resume & Job Matching",
            "Candidate Shortlisting",
            "Interview Scheduler",
            "Email Draft Generator"
        ]
    )
    st.divider()
    st.caption("AI-RH-004 | Student Code: DAS011046")

# Demo candidate data
demo_candidates = [
    {
        "Name": "Aarav Kumar",
        "Email": "aarav@example.com",
        "Resume": "Python, SQL, Pandas, NumPy, Machine Learning, Data Analysis"
    },
    {
        "Name": "Diya Sharma",
        "Email": "diya@example.com",
        "Resume": "Python, Excel, SQL, Statistics, Data Science, Power BI"
    },
    {
        "Name": "Rohan Patel",
        "Email": "rohan@example.com",
        "Resume": "HTML, CSS, JavaScript, React, Git"
    },
    {
        "Name": "Meera Reddy",
        "Email": "meera@example.com",
        "Resume": "Python, Machine Learning, Deep Learning, NLP, Scikit-learn"
    },
    {
        "Name": "Arjun Rao",
        "Email": "arjun@example.com",
        "Resume": "Java, SQL, AWS, Python, Communication"
    }
]

if "candidates" not in st.session_state:
    st.session_state.candidates = pd.DataFrame(demo_candidates)

if "job_description" not in st.session_state:
    st.session_state.job_description = (
        "We need a Data Science Intern skilled in Python, SQL, Pandas, "
        "Machine Learning, Statistics, and Data Analysis."
    )

candidates = st.session_state.candidates.copy()
job_description = st.session_state.job_description
job_skills = extract_skills(job_description)

if page == "Dashboard":
    st.header("Recruitment Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Candidates", len(candidates))
    c2.metric("Required Skills", len(job_skills))
    c3.metric(
        "Shortlisted",
        int((candidates["Status"] == "Shortlisted").sum())
        if "Status" in candidates.columns else 0
    )
    c4.metric("Job Match Ready", "Yes" if job_skills else "Add skills")

    st.subheader("Current Job Description")
    st.write(job_description)
    st.write("**Skills identified:**", ", ".join(job_skills) or "No skills identified yet")

    st.subheader("Candidate Overview")
    st.dataframe(candidates[["Name", "Email", "Resume"]], use_container_width=True)

    st.info("This application includes sample candidate data for demonstration. Replace it with real, authorized candidate information.")

elif page == "Resume & Job Matching":
    st.header("Resume & Job Description Analysis")

    st.subheader("1. Enter the job description")
    new_jd = st.text_area(
        "Job description",
        value=job_description,
        height=140
    )
    if st.button("Analyze Job Description"):
        st.session_state.job_description = new_jd
        st.rerun()

    job_skills = extract_skills(st.session_state.job_description)
    st.write("**Required skills detected:**", ", ".join(job_skills) or "No supported skills detected.")

    st.divider()
    st.subheader("2. Add a candidate resume")

    with st.form("candidate_form"):
        candidate_name = st.text_input("Candidate name")
        candidate_email = st.text_input("Candidate email")
        resume_text = st.text_area(
            "Paste resume text",
            height=160,
            placeholder="Paste the candidate's resume text here..."
        )
        add_candidate = st.form_submit_button("Add Candidate")

    if add_candidate:
        if not candidate_name.strip() or not resume_text.strip():
            st.error("Please enter the candidate's name and resume text.")
        else:
            new_row = pd.DataFrame([{
                "Name": candidate_name.strip(),
                "Email": candidate_email.strip(),
                "Resume": resume_text.strip()
            }])
            st.session_state.candidates = pd.concat(
                [st.session_state.candidates, new_row],
                ignore_index=True
            )
            st.success("Candidate added successfully.")
            st.rerun()

    st.divider()
    st.subheader("3. Match candidates to the job")

    candidates = st.session_state.candidates.copy()
    candidates["Extracted Skills"] = candidates["Resume"].apply(extract_skills)
    candidates["Match Score (%)"] = candidates["Extracted Skills"].apply(
        lambda skills: calculate_match(skills, job_skills)
    )
    candidates = candidates.sort_values("Match Score (%)", ascending=False)

    display = candidates.copy()
    display["Extracted Skills"] = display["Extracted Skills"].apply(
        lambda skills: ", ".join(skills)
    )
    st.dataframe(display, use_container_width=True)

    st.download_button(
        "Download Matching Results (CSV)",
        data=display.to_csv(index=False).encode("utf-8"),
        file_name="candidate_matching_results.csv",
        mime="text/csv"
    )

elif page == "Candidate Shortlisting":
    st.header("Candidate Ranking & Shortlisting")

    candidates = st.session_state.candidates.copy()
    job_skills = extract_skills(st.session_state.job_description)
    candidates["Extracted Skills"] = candidates["Resume"].apply(extract_skills)
    candidates["Match Score (%)"] = candidates["Extracted Skills"].apply(
        lambda skills: calculate_match(skills, job_skills)
    )
    candidates = candidates.sort_values("Match Score (%)", ascending=False)

    threshold = st.slider("Minimum match score for shortlisting (%)", 0, 100, 40)
    candidates["Status"] = candidates["Match Score (%)"].apply(
        lambda score: "Shortlisted" if score >= threshold else "Not shortlisted"
    )

    st.dataframe(
        candidates[["Name", "Email", "Extracted Skills", "Match Score (%)", "Status"]]
        .assign(**{"Extracted Skills": lambda df: df["Extracted Skills"].apply(
            lambda skills: ", ".join(skills)
        )}),
        use_container_width=True
    )

    st.session_state.candidates = candidates.drop(
        columns=["Extracted Skills", "Match Score (%)"], errors="ignore"
    )

    st.download_button(
        "Download Shortlist (CSV)",
        data=candidates.to_csv(index=False).encode("utf-8"),
        file_name="candidate_shortlist.csv",
        mime="text/csv"
    )
    st.caption("The score measures keyword overlap only. Review resumes and make final hiring decisions fairly; it is not a validated measure of candidate ability.")

elif page == "Interview Scheduler":
    st.header("Interview Scheduler")

    candidates = st.session_state.candidates
    names = candidates["Name"].dropna().tolist()

    if not names:
        st.warning("Add a candidate before scheduling an interview.")
    else:
        with st.form("interview_form"):
            selected_candidate = st.selectbox("Candidate", names)
            interview_date = st.date_input("Interview date", value=date.today())
            interview_time = st.time_input("Interview time", value=time(10, 0))
            interviewer = st.text_input("Interviewer name")
            interview_type = st.selectbox(
                "Interview type",
                ["Technical", "HR", "Managerial", "General"]
            )
            meeting_link = st.text_input("Meeting link or location")
            save_interview = st.form_submit_button("Prepare Interview Details")

        if save_interview:
            st.session_state["interview_details"] = {
                "Candidate": selected_candidate,
                "Date": str(interview_date),
                "Time": str(interview_time),
                "Interviewer": interviewer,
                "Type": interview_type,
                "Meeting Link / Location": meeting_link
            }
            st.success("Interview details prepared.")
            st.json(st.session_state["interview_details"])
            st.info("This prepares the schedule details; it does not create a calendar event or send an invitation.")

elif page == "Email Draft Generator":
    st.header("Recruitment Email Draft Generator")

    candidates = st.session_state.candidates
    names = candidates["Name"].dropna().tolist()

    if not names:
        st.warning("Add a candidate before generating an email.")
    else:
        selected_candidate = st.selectbox("Choose candidate", names)
        email_type = st.selectbox(
            "Email purpose",
            [
                "Interview Invitation",
                "Shortlist Notification",
                "Application Update"
            ]
        )
        role = st.text_input("Job title", value="Data Science Intern")
        sender = st.text_input("Recruiter's name", value="Recruitment Team")

        candidate_rows = candidates[candidates["Name"] == selected_candidate]
        candidate_email = candidate_rows.iloc[0]["Email"]

        if email_type == "Interview Invitation":
            subject = f"Interview Invitation - {role}"
            body = (
                f"Dear {selected_candidate},\n\n"
                f"Thank you for applying for the {role} position. "
                "We would like to invite you for an interview.\n\n"
                "Please reply to confirm your availability. The interview "
                "date, time, and meeting details will be shared separately.\n\n"
                f"Regards,\n{sender}"
            )
        elif email_type == "Shortlist Notification":
            subject = f"Application Update - {role}"
            body = (
                f"Dear {selected_candidate},\n\n"
                f"We are pleased to inform you that your application for "
                f"the {role} position has been shortlisted. "
                "Our team will contact you with the next steps.\n\n"
                f"Regards,\n{sender}"
            )
        else:
            subject = f"Application Status - {role}"
            body = (
                f"Dear {selected_candidate},\n\n"
                f"Thank you for your interest in the {role} position. "
                "Your application is being reviewed. We will share an update "
                "when further information is available.\n\n"
                f"Regards,\n{sender}"
            )

        st.text_input("Recipient email", value=candidate_email, key="draft_recipient")
        st.text_input("Subject", value=subject, key="draft_subject")
        st.text_area("Email body", value=body, height=220, key="draft_body")

        st.download_button(
            "Download Email Draft",
            data=(
                f"To: {st.session_state.draft_recipient}\n"
                f"Subject: {st.session_state.draft_subject}\n\n"
                f"{st.session_state.draft_body}"
            ),
            file_name="recruitment_email_draft.txt",
            mime="text/plain"
        )
        st.caption("This tool creates a draft only. It does not send emails.")
