import streamlit as st
from model import compute_score
from utils import extract_text

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI Resume Screening System")
st.write("Match resumes with job descriptions using AI")

uploaded_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)
        score, device = compute_score(resume_text, job_desc)

        st.success(f"Match Score: {round(score*100,2)}%")
        st.info(f"Running on: {device}")
    else:
        st.warning("Please upload resume and enter job description")