from db_connect import get_connection
from parser import parse_resume
from vectorizer import get_top_jobs

conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT id, title, description FROM jobs")
rows = cur.fetchall()

job_ids, job_titles, job_descriptions = zip(*rows)
resume_raw = open("data/sample_resume.txt").read()
parsed_resume = parse_resume(resume_raw)

top_indices, scores = get_top_jobs(parsed_resume, list(job_descriptions))

print("\nTop matching jobs:")
for i in top_indices:
    print(f"{job_titles[i]} (Score: {scores[i]:.2f})")
