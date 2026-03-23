import sys
import os
import psycopg2 
from app.config import DATABASE_URL

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def setup():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_chunks (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            embedding vector(384)
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database setup completed.")

if __name__ == "__main__":
    setup()