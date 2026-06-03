"""
練習 3：成績統計系統 ⭐⭐⭐

任務：
建立學生成績管理系統，包含多個資料表和統計功能。

要求：
1. 建立三個資料表：
   - students: 學生資料（學號、姓名、班級）
   - subjects: 科目資料（科目代碼、科目名稱）
   - scores: 成績資料（學號、科目代碼、成績）
2. 實作功能：
   - 新增學生、科目、成績
   - 查詢學生的所有成績
   - 計算學生的平均成績
   - 統計科目的平均分數
   - 找出每個科目的最高分學生
   - 列出不及格（< 60）的成績記錄

提示：
- 使用 JOIN 連接多個資料表
- 使用 GROUP BY 進行分組統計
- 使用子查詢找出最高分
"""

import sqlite3


class GradeManager:
    """成績管理系統"""

    def __init__(self, db_name="grades.db"):
        """初始化成績管理系統"""
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        """建立資料表"""
        cursor = self.conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS scores")
        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute("DROP TABLE IF EXISTS subjects")

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                class_name TEXT NOT NULL
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS subjects (
                subject_code TEXT PRIMARY KEY,
                subject_name TEXT NOT NULL
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                subject_code TEXT NOT NULL,
                score REAL NOT NULL CHECK(score >= 0 AND score <= 100),
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (subject_code) REFERENCES subjects(subject_code)
            )
        """
        )
        self.conn.commit()

    def add_student(self, student_id, name, class_name):
        """新增學生"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO students (student_id, name, class_name) VALUES (?, ?, ?)",
            (student_id, name, class_name),
        )
        self.conn.commit()
        print(f"  ✓ 新增學生：{name}（{student_id}）")

    def add_subject(self, subject_code, subject_name):
        """新增科目"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO subjects (subject_code, subject_name) VALUES (?, ?)",
            (subject_code, subject_name),
        )
        self.conn.commit()
        print(f"  ✓ 新增科目：{subject_name}（{subject_code}）")

    def add_score(self, student_id, subject_code, score):
        """新增成績"""
        cursor = self.conn.cursor()

        # 確認學生存在
        cursor.execute("SELECT name FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        if not student:
            print(f"  ✗ 學號 {student_id} 不存在")
            return

        # 確認科目存在
        cursor.execute("SELECT subject_name FROM subjects WHERE subject_code = ?", (subject_code,))
        subject = cursor.fetchone()
        if not subject:
            print(f"  ✗ 科目代碼 {subject_code} 不存在")
            return

        if not (0 <= score <= 100):
            print(f"  ✗ 成績必須介於 0~100 之間")
            return

        cursor.execute(
            "INSERT INTO scores (student_id, subject_code, score) VALUES (?, ?, ?)",
            (student_id, subject_code, score),
        )
        self.conn.commit()
        print(f"  ✓ 新增成績：{student[0]} / {subject[0]} = {score}")

    def get_student_scores(self, student_id):
        """查詢學生的所有成績"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT sub.subject_name, sc.score
            FROM scores sc
            JOIN subjects sub ON sc.subject_code = sub.subject_code
            WHERE sc.student_id = ?
            ORDER BY sub.subject_name
        """,
            (student_id,),
        )
        rows = cursor.fetchall()
        if not rows:
            print(f"  查無學號 {student_id} 的成績資料")
            return
        print(f"  {'科目':<15} {'成績':>8}")
        print(f"  {'-'*24}")
        for subject_name, score in rows:
            print(f"  {subject_name:<15} {score:>8.1f}")

    def calculate_student_average(self, student_id):
        """計算學生的平均成績"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT AVG(score) FROM scores WHERE student_id = ?",
            (student_id,),
        )
        result = cursor.fetchone()[0]
        return result if result is not None else 0.0

    def calculate_subject_average(self, subject_code):
        """計算科目的平均分數"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT AVG(score) FROM scores WHERE subject_code = ?",
            (subject_code,),
        )
        result = cursor.fetchone()[0]
        return result if result is not None else 0.0

    def find_top_students_by_subject(self):
        """找出每個科目的最高分學生"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT sub.subject_name, st.name, sc.score
            FROM scores sc
            JOIN students st ON sc.student_id = st.student_id
            JOIN subjects sub ON sc.subject_code = sub.subject_code
            WHERE sc.score = (
                SELECT MAX(score) FROM scores s2
                WHERE s2.subject_code = sc.subject_code
            )
            ORDER BY sub.subject_name
        """
        )
        rows = cursor.fetchall()
        print(f"  {'科目':<15} {'學生':<10} {'最高分':>8}")
        print(f"  {'-'*34}")
        for subject_name, name, score in rows:
            print(f"  {subject_name:<15} {name:<10} {score:>8.1f}")

    def find_failing_scores(self):
        """列出不及格的成績記錄"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT st.name, sub.subject_name, sc.score
            FROM scores sc
            JOIN students st ON sc.student_id = st.student_id
            JOIN subjects sub ON sc.subject_code = sub.subject_code
            WHERE sc.score < 60
            ORDER BY sc.score
        """
        )
        rows = cursor.fetchall()
        if not rows:
            print("  沒有不及格的成績記錄 🎉")
            return
        print(f"  {'學生':<10} {'科目':<15} {'成績':>8}")
        print(f"  {'-'*34}")
        for name, subject_name, score in rows:
            print(f"  {name:<10} {subject_name:<15} {score:>8.1f}  ✗ 不及格")

    def close(self):
        """關閉資料庫連接"""
        self.conn.close()


def main():
    """主程式"""
    print("成績統計系統")
    print("=" * 60)

    manager = GradeManager()

    print("\n【新增學生】")
    manager.add_student("S001", "王小明", "一年A班")
    manager.add_student("S002", "李小華", "一年A班")
    manager.add_student("S003", "張大同", "一年B班")

    print("\n【新增科目】")
    manager.add_subject("MATH", "數學")
    manager.add_subject("ENG", "英文")
    manager.add_subject("PHY", "物理")

    print("\n【新增成績】")
    manager.add_score("S001", "MATH", 85)
    manager.add_score("S001", "ENG", 78)
    manager.add_score("S001", "PHY", 92)
    manager.add_score("S002", "MATH", 92)
    manager.add_score("S002", "ENG", 55)
    manager.add_score("S002", "PHY", 88)
    manager.add_score("S003", "MATH", 76)
    manager.add_score("S003", "ENG", 82)
    manager.add_score("S003", "PHY", 58)

    print("\n【王小明的成績】")
    manager.get_student_scores("S001")

    print("\n【平均成績】")
    avg = manager.calculate_student_average("S001")
    print(f"  王小明的平均成績: {avg:.2f}")

    print("\n【數學科平均】")
    avg = manager.calculate_subject_average("MATH")
    print(f"  數學平均分數: {avg:.2f}")

    print("\n【各科最高分】")
    manager.find_top_students_by_subject()

    print("\n【不及格記錄】")
    manager.find_failing_scores()

    manager.close()


if __name__ == "__main__":
    main()
