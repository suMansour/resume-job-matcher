from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_top_jobs(resume_text, job_descriptions, top_n=3):
    vectorizer = TfidfVectorizer()
    all_docs = job_descriptions + [resume_text]
    vectors = vectorizer.fit_transform(all_docs)
    scores = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    top_indices = scores.argsort()[-top_n:][::-1]
    return top_indices, scores
