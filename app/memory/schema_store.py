from app.db.connection import get_db_connection

def save_chunk(content: str, embedding: list):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO schema_chunks (content, embedding) VALUES (%s, %s)",
        (content, embedding)
    )
    conn.commit()
    cursor.close()
    conn.close()

def search_chunks(question_embedding: list, top_k: int = 3) -> list:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT content FROM schema_chunks
        ORDER BY embedding <-> %s::vector
        LIMIT %s
        """,
        (question_embedding, top_k)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in rows]