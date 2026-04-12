# 🚀 AI Resume Screening System (AMD AI Engage)

## 📌 Overview
This project is an AI-powered Resume Screening Web Application that automates candidate shortlisting using Natural Language Processing (NLP). It compares resumes with job descriptions and generates a match score to help recruiters identify the best candidates efficiently.

---

## 🎯 Features
- 📄 Upload Resume (PDF / TXT)
- 📝 Input Job Description
- 📊 Match Score Calculation
- ⚡ GPU-ready computation using PyTorch
- 🌐 Interactive Web UI using Streamlit

---

## 🧠 How It Works
1. Resume and job description are processed as text
2. TF-IDF vectorization converts text into numerical form
3. Cosine similarity calculates match score
4. Output shows percentage match and device used

---

## ⚙️ Tech Stack
- Python
- Streamlit (Frontend UI)
- Scikit-learn (TF-IDF Vectorization)
- PyTorch (GPU Acceleration Support)

---

## ⚡ GPU Acceleration (AMD Focus)
This project is designed to support GPU acceleration using PyTorch.

- Uses tensor-based computation for similarity scoring
- Automatically detects GPU availability
- Compatible with:
  - NVIDIA CUDA GPUs
  - AMD GPUs via ROCm (Linux-based systems)

> Note: Current demo runs on CPU due to hardware limitations, but the system is fully GPU-compatible and scales efficiently when deployed on GPU-enabled environments.

---

## 🧪 Demo

### Input:
- Resume uploaded via UI
- Job description entered manually

### Output:
- Match Score (e.g., 82.34%)
- Device Info (CPU / GPU-ready)

---


## 🖥️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 Demo Screenshot

![Demo](resume_output.png)

---

## 🔮 Future Enhancements

- BERT-based semantic matching  
- Batch resume processing (strong GPU use case)  
- Cloud deployment  
- Recruiter analytics dashboard  

---

## 📚 Use Case

- HR Tech / Recruitment Automation  
- AI-based Candidate Screening  
- Data-driven Hiring Systems  

---

## 👨‍💻 Author

Aryan Shete  
AI & Data Science Student
