"""example02_crud_operations.py

示範完整的 CRUD（增刪改查）操作
"""

import sqlite3


class StudentDatabase:
    """學生資料庫管理類別"""

    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """連接資料庫"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f"✓ 已連接到資料庫：{self.db_name}")

    def close(self):
        """關閉資料庫連接"""
        if self.conn:
            self.conn.close()
            print("✓ 資料庫連接已關閉")

    def create_table(self):
        """建立資料表"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT
            )
        """
        )
        self.conn.commit()
        print("✓ 資料表已建立")

    def create(self, student_id, name, age, email):
        """新增學生（Create）"""
        try:
            self.cursor.execute(
                """
                INSERT INTO students (student_id, name, age, email)
                VALUES (?, ?, ?, ?)
            """,
                (student_id, name, age, email),
            )
            self.conn.commit()
            print(f"✓ 新增學生：{name} ({student_id})")
            return True
        except sqlite3.IntegrityError:
            print(f"✗ 錯誤：學號 {student_id} 已存在")
            return False

    def read_all(self):
        """查詢所有學生（Read）"""
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def read_by_id(self, student_id):
        """根據學號查詢學生（Read）"""
        self.cursor.execute(
            """
            SELECT * FROM students
            WHERE student_id = ?
        """,
            (student_id,),
        )
        return self.cursor.fetchone()

    def update(self, student_id, **kwargs):
        """更新學生資料（Update）"""
        # 動態建立 UPDATE 語句
        fields = []
        values = []

        for key, value in kwargs.items():
            if key in ["name", "age", "email"]:
                fields.append(f"{key} = ?")
                values.append(value)

        if not fields:
            print("✗ 沒有要更新的欄位")
            return False

        values.append(student_id)
        sql = f"UPDATE students SET {', '.join(fields)} WHERE student_id = ?"

        self.cursor.execute(sql, values)
        self.conn.commit()

        if self.cursor.rowcount > 0:
            print(f"✓ 更新學生：{student_id}")
            return True
        else:
            print(f"✗ 找不到學號：{student_id}")
            return False

    def delete(self, student_id):
        """刪除學生（Delete）"""
        self.cursor.execute(
            """
            DELETE FROM students
            WHERE student_id = ?
        """,
            (student_id,),
        )
        self.conn.commit()

        if self.cursor.rowcount > 0:
            print(f"✓ 刪除學生：{student_id}")
            return True
        else:
            print(f"✗ 找不到學號：{student_id}")
            return False

    def display_all(self):
        """顯示所有學生"""
        students = self.read_all()

        if not students:
            print("目前沒有學生資料")
            return

        print(f"\n{'ID':<5} {'學號':<10} {'姓名':<10} {'年齡':<6} {'Email':<25}")
        print("-" * 60)

        for student in students:
            print(
                f"{student[0]:<5} {student[1]:<10} {student[2]:<10} "
                f"{student[3]:<6} {student[4]:<25}"
            )


def demo_crud():
    """示範完整的 CRUD 操作"""

    # 建立資料庫實例
    db = StudentDatabase("crud_demo.db")
    db.connect()
    db.create_table()

    print("\n=== CREATE（新增）===")
    db.create("S001", "小明", 20, "ming@example.com")
    db.create("S002", "小美", 19, "mei@example.com")
    db.create("S003", "阿強", 21, "qiang@example.com")
    db.create("S001", "重複", 20, "duplicate@example.com")  # 會失敗

    print("\n=== READ（查詢所有）===")
    db.display_all()

    print("\n=== READ（查詢單筆）===")
    student = db.read_by_id("S002")
    if student:
        print(f"找到學生：{student[2]} ({student[1]})")

    print("\n=== UPDATE（更新）===")
    db.update("S001", age=21, email="ming_new@example.com")
    db.update("S999", name="不存在")  # 會失敗

    print("\n=== 更新後的資料 ===")
    db.display_all()

    print("\n=== DELETE（刪除）===")
    db.delete("S003")
    db.delete("S999")  # 會失敗

    print("\n=== 刪除後的資料 ===")
    db.display_all()

    db.close()


if __name__ == "__main__":
    demo_crud()
    print("\n=== 完成 ===")
