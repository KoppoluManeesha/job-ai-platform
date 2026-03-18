import sqlite3

conn = sqlite3.connect("data/jobs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    link TEXT,
    score INTEGER,
    fresher TEXT,
    missing_skills TEXT,
    reason TEXT
)
""")

def insert_job(job):
    cursor.execute("""
    INSERT INTO jobs (title, company, location, link, score, fresher, missing_skills, reason)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, job)
    conn.commit()