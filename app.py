import streamlit as st
from analyzer import (
    extract_text_from_pdf,
    extract_skills,
    calculate_similarity,
    clean_text
)

st.set_page_config(page_title="AI Resume Skill Gap Analyzer")

st.title("📄 AI Resume Skill Gap Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    resume_text = extract_text_from_pdf(resume_file)
    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    missing_skills = job_skills - resume_skills
    similarity = calculate_similarity(resume_text, job_desc)

    st.subheader("✅ Matched Skills")
    st.write(list(resume_skills & job_skills))

    st.subheader("❌ Missing Skills")
    st.write(list(missing_skills))

    st.metric("📊 Resume Match %", f"{similarity:.2f}%")
