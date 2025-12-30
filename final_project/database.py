"""
資料庫操作模組
處理 SQLite 資料庫的 CRUD 操作
"""

import sqlite3
from models import Student, Subject, Grade


class Database:
    """資料庫管理類別"""

    def __init__(self, db_name="student_system.db"):
        self.db_name = db_name
        self.init_database()

    def get_connection(self):
        """取得資料庫連線"""
        return sqlite3.connect(self.db_name)

    def init_database(self):
        """初始化資料庫，建立所需的資料表"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 建立學生資料表
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT
            )
        """
        )

        # 建立科目資料表
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS subjects (
                subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_name TEXT NOT NULL UNIQUE,
                credits INTEGER
            )
        """
        )

        # 建立成績資料表
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS grades (
                grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject_id INTEGER,
                score REAL,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
                UNIQUE(student_id, subject_id)
            )
        """
        )

        conn.commit()
        conn.close()

    # ==================== 學生 CRUD ====================

    def create_student(self, name, age, email):
        """新增學生"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
                (name, age, email),
            )
            conn.commit()
            student_id = cursor.lastrowid
            return student_id
        except sqlite3.Error as e:
            print(f"新增學生失敗: {e}")
            return None
        finally:
            conn.close()

    def get_all_students(self):
        """取得所有學生"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()

        students = []
        for row in rows:
            student = Student(student_id=row[0], name=row[1], age=row[2], email=row[3])
            students.append(student)
        return students

    def get_student_by_id(self, student_id):
        """根據 ID 取得學生"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Student(student_id=row[0], name=row[1], age=row[2], email=row[3])
        return None

    def update_student(self, student_id, name=None, age=None, email=None):
        """更新學生資料"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 先取得現有資料
        student = self.get_student_by_id(student_id)
        if not student:
            conn.close()
            return False

        # 使用新值或保留舊值
        new_name = name if name is not None else student.name
        new_age = age if age is not None else student.age
        new_email = email if email is not None else student.email

        try:
            cursor.execute(
                "UPDATE students SET name = ?, age = ?, email = ? WHERE student_id = ?",
                (new_name, new_age, new_email, student_id),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"更新學生失敗: {e}")
            return False
        finally:
            conn.close()

    def delete_student(self, student_id):
        """刪除學生"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            # 先刪除相關成績
            cursor.execute("DELETE FROM grades WHERE student_id = ?", (student_id,))
            # 刪除學生
            cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"刪除學生失敗: {e}")
            return False
        finally:
            conn.close()

    # ==================== 科目 CRUD ====================

    def create_subject(self, subject_name, credits):
        """新增科目"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO subjects (subject_name, credits) VALUES (?, ?)",
                (subject_name, credits),
            )
            conn.commit()
            subject_id = cursor.lastrowid
            return subject_id
        except sqlite3.IntegrityError:
            print(f"科目 '{subject_name}' 已存在！")
            return None
        except sqlite3.Error as e:
            print(f"新增科目失敗: {e}")
            return None
        finally:
            conn.close()

    def get_all_subjects(self):
        """取得所有科目"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subjects")
        rows = cursor.fetchall()
        conn.close()

        subjects = []
        for row in rows:
            subject = Subject(subject_id=row[0], subject_name=row[1], credits=row[2])
            subjects.append(subject)
        return subjects

    def get_subject_by_id(self, subject_id):
        """根據 ID 取得科目"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subjects WHERE subject_id = ?", (subject_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Subject(subject_id=row[0], subject_name=row[1], credits=row[2])
        return None

    def update_subject(self, subject_id, subject_name=None, credits=None):
        """更新科目資料"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 先取得現有資料
        subject = self.get_subject_by_id(subject_id)
        if not subject:
            conn.close()
            return False

        # 使用新值或保留舊值
        new_name = subject_name if subject_name is not None else subject.subject_name
        new_credits = credits if credits is not None else subject.credits

        try:
            cursor.execute(
                "UPDATE subjects SET subject_name = ?, credits = ? WHERE subject_id = ?",
                (new_name, new_credits, subject_id),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"更新科目失敗: {e}")
            return False
        finally:
            conn.close()

    def delete_subject(self, subject_id):
        """刪除科目"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            # 先刪除相關成績
            cursor.execute("DELETE FROM grades WHERE subject_id = ?", (subject_id,))
            # 刪除科目
            cursor.execute("DELETE FROM subjects WHERE subject_id = ?", (subject_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"刪除科目失敗: {e}")
            return False
        finally:
            conn.close()

    # ==================== 成績操作 ====================

    def add_grade(self, student_id, subject_id, score):
        """新增或更新成績"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT OR REPLACE INTO grades (student_id, subject_id, score) VALUES (?, ?, ?)",
                (student_id, subject_id, score),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"新增成績失敗: {e}")
            return False
        finally:
            conn.close()

    def get_grades_by_subject(self, subject_id):
        """取得特定科目的所有成績（含學生資訊），按分數排名"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT s.student_id, s.name, g.score, subj.subject_name
            FROM grades g
            JOIN students s ON g.student_id = s.student_id
            JOIN subjects subj ON g.subject_id = subj.subject_id
            WHERE g.subject_id = ?
            ORDER BY g.score DESC
        """,
            (subject_id,),
        )
        rows = cursor.fetchall()
        conn.close()

        results = []
        for idx, row in enumerate(rows, 1):
            results.append(
                {
                    "rank": idx,
                    "student_id": row[0],
                    "student_name": row[1],
                    "score": row[2],
                    "subject_name": row[3],
                }
            )
        return results

    def get_student_grades(self, student_id):
        """取得特定學生的所有成績"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT subj.subject_name, g.score, subj.credits
            FROM grades g
            JOIN subjects subj ON g.subject_id = subj.subject_id
            WHERE g.student_id = ?
        """,
            (student_id,),
        )
        rows = cursor.fetchall()
        conn.close()

        results = []
        for row in rows:
            results.append({"subject_name": row[0], "score": row[1], "credits": row[2]})
        return results

    def get_all_data(self):
        """取得所有資料（用於備份）"""
        return {
            "students": [s.to_dict() for s in self.get_all_students()],
            "subjects": [s.to_dict() for s in self.get_all_subjects()],
            "grades": self.get_all_grades_raw(),
        }

    def get_all_grades_raw(self):
        """取得所有成績的原始資料"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grades")
        rows = cursor.fetchall()
        conn.close()

        grades = []
        for row in rows:
            grades.append(
                {
                    "grade_id": row[0],
                    "student_id": row[1],
                    "subject_id": row[2],
                    "score": row[3],
                }
            )
        return grades
