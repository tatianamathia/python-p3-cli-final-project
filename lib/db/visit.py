from .config import get_db

class Visit:
    @staticmethod
    def create(student_id, medical_issue_id, date):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO visits (student_id, date, medical_issue_id) VALUES (?, ?, ?)', (student_id, date, medical_issue_id))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def delete(visit_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM visits WHERE id = ?', (visit_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, student_id, date, medical_issue_id FROM visits')
            return cursor.fetchall()

    @staticmethod
    def find_by_id(visit_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, student_id, date, medical_issue_id FROM visits WHERE id = ?', (visit_id,))
            return cursor.fetchone()
