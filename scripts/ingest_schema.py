import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.memory.embedder import embed
from app.memory.schema_store import save_chunk

def load_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def split_sql_chunks(sql: str) -> list:
    chunks = []
    current = ""
    for line in sql.splitlines():
        current += line + "\n"
        if line.strip().endswith(";"):
            if current.strip():
                chunks.append(current.strip())
            current = ""
    return chunks

def ingest():
    print("Loading schema files...")

    sql = load_file("schema/tables.sql")
    notes = load_file("schema/notes.md")

    sql_chunks = split_sql_chunks(sql)
    notes_chunks = [notes]

    all_chunks = sql_chunks + notes_chunks

    print(f"Found {len(all_chunks)} chunks to ingest...")

    for i, chunk in enumerate(all_chunks):
        print(f"Embedding chunk {i + 1}/{len(all_chunks)}...")
        embedding = embed(chunk)
        save_chunk(chunk, embedding)

    print("Ingestion complete")

if __name__ == "__main__":
    ingest()