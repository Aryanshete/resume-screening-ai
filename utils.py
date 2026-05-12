import PyPDF2
import re

TECH_KEYWORDS = {
    "AI / ML": [
        "machine learning",
        "deep learning",
        "nlp",
        "computer vision",
        "llm",
        "rag",
        "agentic ai",
        "transformers",
        "hugging face",
        "pytorch",
        "tensorflow",
        "scikit-learn",
        "langchain",
        "prompt engineering"
    ],
    "Programming": [
        "python",
        "java",
        "c++",
        "javascript",
        "sql",
        "php"
    ],
    "Backend / APIs": [
        "django",
        "flask",
        "fastapi",
        "node.js",
        "express",
        "rest api",
        "api integration"
    ],
    "Databases": [
        "mysql",
        "mongodb",
        "postgresql",
        "supabase",
        "pinecone",
        "faiss",
        "chroma",
        "vector database"
    ],
    "Cloud / DevOps": [
        "aws",
        "docker",
        "git",
        "github",
        "vercel"
    ]
}

def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        return text

    return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

def extract_keywords(text):
    text = clean_text(text)
    found = set()

    for category in TECH_KEYWORDS.values():
        for keyword in category:
            if keyword in text:
                found.add(keyword)

    return found

def get_skill_match(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords

    if len(jd_keywords) == 0:
        score = 0
    else:
        score = (len(matched) / len(jd_keywords)) * 100

    return matched, missing, score