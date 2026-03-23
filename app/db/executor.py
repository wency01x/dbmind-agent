from app.db.connection import get_db_connection

def run_query(sql: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows