import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def insert_jobs():
    # Establish DB connection
    conn = psycopg2.connect(
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT")
    )
    cursor = conn.cursor()

    # Sample job data
    jobs = [
        ('Software Engineer', 'Google', 'New York, NY', 'Develop and maintain software applications.'),
        ('Data Scientist', 'Facebook', 'San Francisco, CA', 'Analyze large datasets and build predictive models.'),
        ('Product Manager', 'Amazon', 'Seattle, WA', 'Oversee the development and launch of new products.'),
        ('Web Developer', 'Apple', 'Cupertino, CA', 'Build and maintain websites and web applications.'),
        ('Data Engineer', 'Microsoft', 'Redmond, WA', 'Design and build data pipelines and ETL processes.'),
        ('Marketing Manager', 'Netflix', 'Los Angeles, CA', 'Lead marketing campaigns and strategy.'),
        ('UX Designer', 'Adobe', 'San Jose, CA', 'Design user-friendly interfaces for digital products.'),
        ('HR Specialist', 'Tesla', 'Austin, TX', 'Manage recruiting, employee relations, and HR processes.'),
        ('Business Analyst', 'IBM', 'Chicago, IL', 'Analyze business processes and recommend improvements.'),
        ('QA Engineer', 'Spotify', 'Stockholm, SE', 'Test software and ensure quality standards are met.')
    ]

    # Insert job data into the jobs table
    cursor.executemany('''
        INSERT INTO jobs (title, company, location, description)
        VALUES (%s, %s, %s, %s)
    ''', jobs)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_jobs()
