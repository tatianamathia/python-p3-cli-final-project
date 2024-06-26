from .config import get_db

class Visit:
    @classmethod
    def create(cls, student_id, medical_issue_id, date):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO visits (student_id, date, medical_issue_id) VALUES (?, ?, ?)', (student_id, date, medical_issue_id))
            conn.commit()
            return cursor.lastrowid

    @classmethod
    def delete(cls, visit_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM visits WHERE id = ?', (visit_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, student_id, date, medical_issue_id FROM visits')
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, visit_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, student_id, date, medical_issue_id FROM visits WHERE id = ?', (visit_id,))
            return cursor.fetchone()
