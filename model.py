import torch
from sklearn.feature_extraction.text import TfidfVectorizer

def get_device():
    if torch.cuda.is_available():
        return torch.device("cuda"), "GPU (CUDA/ROCm)"
    else:
        return torch.device("cpu"), "CPU (GPU-ready)"

def compute_score(resume, job_desc):
    documents = [resume, job_desc]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents).toarray()

    # Get device
    device, device_name = get_device()

    tfidf_tensor = torch.tensor(tfidf_matrix, dtype=torch.float32).to(device)

    score = torch.nn.functional.cosine_similarity(
        tfidf_tensor[0].unsqueeze(0),
        tfidf_tensor[1].unsqueeze(0)
    )

    return score.item(), device_name