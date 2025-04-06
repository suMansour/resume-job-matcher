# Resume Job Matcher

A smart resume screening tool that recommends top matching jobs using NLP and scikit-learn.

## Features

- Resume parsing using spaCy
- Job similarity using TF-IDF + cosine similarity
- PostgreSQL DB on Railway

## How to Run

1. Clone repo
2. Set up `.env` or edit DB creds in `db_connect.py`
3. Run `python src/main.py`
