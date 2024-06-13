from .config import get_db

class Student:
    @classmethod
    def create(cls, name, gender):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO students (name, gender) VALUES (?, ?)', (name, gender))
            conn.commit()
            return cursor.lastrowid

    @classmethod
    def delete(cls, student_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, gender FROM students')
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, student_id):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, gender FROM students WHERE id = ?', (student_id,))
            return cursor.fetchone()
