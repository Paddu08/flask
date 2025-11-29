
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("DATABASE_URL")
connection=psycopg2.connect(url)
cursor=connection.cursor()

connection.autocommit = True
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
)
""")
