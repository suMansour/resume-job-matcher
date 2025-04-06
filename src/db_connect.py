import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from the .env file
load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT")
    )
    return conn
