from .config import get_db

class MedicalIssue:
    @staticmethod
    def create(description, severity, treatment):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO medical_issues (description, severity, treatment) VALUES (?, ?, ?)', (description, severity, treatment))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def delete(medical_issue_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM medical_issues WHERE id = ?', (medical_issue_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, description, severity, treatment FROM medical_issues')
            return cursor.fetchall()

    @staticmethod
    def find_by_id(medical_issue_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, description, severity, treatment FROM medical_issues WHERE id = ?', (medical_issue_id,))
            return cursor.fetchone()
