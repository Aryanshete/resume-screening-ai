import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "all-MiniLM-L6-v2"

def get_device():
    if torch.cuda.is_available():
        return "cuda", "GPU (CUDA)"
    return "cpu", "CPU"

model = SentenceTransformer(MODEL_NAME, device=get_device()[0])

def compute_score(resume, job_desc):
    device_name = get_device()[1]

    resume_embedding = model.encode(resume)
    jd_embedding = model.encode(job_desc)

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return score, device_name