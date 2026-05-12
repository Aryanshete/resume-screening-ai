import streamlit as st
from model import compute_score
from utils import extract_text, get_skill_match

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        padding-top: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #b0b0b0;
        text-align: center;
        margin-bottom: 40px;
    }

    .metric-card {
        background: linear-gradient(135deg, #111827, #1f2937);
        padding: 24px;
        border-radius: 18px;
        border: 1px solid #2d3748;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }

    .metric-title {
        font-size: 15px;
        color: #9ca3af;
        margin-bottom: 10px;
    }

    .metric-value {
        font-size: 34px;
        font-weight: 700;
        color: white;
    }

    .section-card {
        background: #111827;
        padding: 28px;
        border-radius: 20px;
        border: 1px solid #2d3748;
        margin-top: 20px;
    }

    .skill-tag {
        display: inline-block;
        padding: 10px 16px;
        margin: 6px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 600;
    }

    .matched {
        background: rgba(34,197,94,0.18);
        color: #86efac;
        border: 1px solid rgba(34,197,94,0.3);
    }

    .missing {
        background: rgba(239,68,68,0.18);
        color: #fca5a5;
        border: 1px solid rgba(239,68,68,0.3);
    }

    .score-label {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">🚀 AI-Powered ATS Resume Analyzer</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="hero-subtitle">Transformer-based semantic resume analysis with ATS compatibility scoring and technical skill gap detection</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "txt"]
    )

with col2:
    job_desc = st.text_area(
        "Paste Job Description",
        height=250,
        placeholder="Paste the job description here..."
    )

if st.button("Analyze Resume", use_container_width=True):

    if uploaded_file and job_desc:

        with st.spinner("Analyzing candidate profile..."):

            resume_text = extract_text(uploaded_file)

            semantic_score, device = compute_score(resume_text, job_desc)

            matched_skills, missing_skills, skill_score = get_skill_match(
                resume_text,
                job_desc
            )

            final_score = (semantic_score * 100 * 0.75) + (skill_score * 0.25)

        st.success("Analysis completed successfully")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Semantic Match</div>
                    <div class="metric-value">{semantic_score * 100:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class="metric-card">
                <div class="metric-title">JD Keyword Match</div>                    <div class="metric-value">{skill_score:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Final ATS Score</div>
                    <div class="metric-value">{final_score:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("### ATS Compatibility Score")

        progress_value = float(min(final_score / 100, 1.0))
        st.progress(progress_value)

        if final_score >= 75:
            st.success("Strong alignment with this role")
        elif final_score >= 50:
            st.warning("Moderate alignment with this role")
        else:
            st.error("Low alignment with this role")

        st.caption(f"Execution Environment: {device}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.subheader("✅ Matching Technical Skills")

            if matched_skills:
                for skill in sorted(matched_skills):
                    display_skill = skill.upper() if skill.lower() == "llm" else skill.title()

                    st.markdown(
                        f'<span class="skill-tag matched">{display_skill}</span>',
                        unsafe_allow_html=True
                    )
            else:
                st.info("No technical overlap detected.")

            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.subheader("⚠ Missing Technical Skills")

            if missing_skills:
                for skill in sorted(list(missing_skills))[:12]:
                    display_skill = skill.upper() if skill.lower() == "llm" else skill.title()

                    st.markdown(
                        f'<span class="skill-tag missing">{skill.title()}</span>',
                        unsafe_allow_html=True
                    )
            else:
                st.success("Excellent alignment with job requirements.")

            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("Please upload a resume and paste a job description.")