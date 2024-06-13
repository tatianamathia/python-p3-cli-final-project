from .config import get_db

class MedicalIssue:
    @classmethod
    def create_medical_issue(cls, description, severity, treatment):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO medical_issues (description, severity, treatment) VALUES (?, ?, ?)', (description, severity, treatment))
            conn.commit()
            return cursor.lastrowid

    @classmethod
    def delete_medical_issue(cls, medical_issue_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM medical_issues WHERE id = ?', (medical_issue_id,))
            conn.commit()

    @classmethod
    def get_all_medical_issues(cls):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, description, severity, treatment FROM medical_issues')
            return cursor.fetchall()

    @classmethod
    def find_medical_issue_by_id(cls, medical_issue_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, description, severity, treatment FROM medical_issues WHERE id = ?', (medical_issue_id,))
            return cursor.fetchone()
