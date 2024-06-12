from .config import get_db

class Student:
    @staticmethod
    def create(name, gender):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO students (name, gender) VALUES (?, ?)', (name, gender))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def delete(student_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, gender FROM students')
            return cursor.fetchall()

    @staticmethod
    def find_by_id(student_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, gender FROM students WHERE id = ?', (student_id,))
            return cursor.fetchone()
