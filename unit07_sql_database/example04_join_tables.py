"""example04_join_tables.py

示範多表關聯查詢（JOIN）
"""

import sqlite3


def setup_database():
    """建立多表關聯的測試資料庫"""
    conn = sqlite3.connect("join_demo.db")
    cursor = conn.cursor()

    # 建立學生表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            class_id INTEGER
        )
    """
    )

    # 建立班級表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL,
            teacher TEXT
        )
    """
    )

    # 建立成績表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT,
            score INTEGER
        )
    """
    )

    # 清空舊資料
    cursor.execute("DELETE FROM students")
    cursor.execute("DELETE FROM classes")
    cursor.execute("DELETE FROM scores")

    # 插入班級資料
    classes = [("一年一班", "王老師"), ("一年二班", "李老師"), ("二年一班", "張老師")]
    cursor.executemany(
        "INSERT INTO classes (class_name, teacher) VALUES (?, ?)", classes
    )

    # 插入學生資料
    students = [("小明", 1), ("小美", 1), ("阿強", 2), ("阿花", 2), ("小華", 3)]
    cursor.executemany("INSERT INTO students (name, class_id) VALUES (?, ?)", students)

    # 插入成績資料
    scores = [
        (1, "國文", 85),
        (1, "英文", 90),
        (1, "數學", 88),
        (2, "國文", 92),
        (2, "英文", 87),
        (2, "數學", 95),
        (3, "國文", 78),
        (3, "英文", 82),
        (4, "國文", 88),
        (4, "數學", 86),
        (5, "國文", 95),
        (5, "英文", 89),
    ]
    cursor.executemany(
        "INSERT INTO scores (student_id, subject, score) VALUES (?, ?, ?)", scores
    )

    conn.commit()
    conn.close()
    print("✓ 多表測試資料已建立")


def demo_inner_join():
    """示範 INNER JOIN（內部連接）"""
    print("\n=== INNER JOIN（內部連接）===")

    conn = sqlite3.connect("join_demo.db")
    cursor = conn.cursor()

    # 查詢學生及其班級資訊
    cursor.execute(
        """
        SELECT students.name, classes.class_name, classes.teacher
        FROM students
        INNER JOIN classes ON students.class_id = classes.id
    """
    )

    rows = cursor.fetchall()
    print("學生班級資訊：")
    for row in rows:
        print(f"  {row[0]} - {row[1]} ({row[2]})")

    conn.close()


def demo_left_join():
    """示範 LEFT JOIN（左外連接）"""
    print("\n=== LEFT JOIN（左外連接）===")

    conn = sqlite3.connect("join_demo.db")
    cursor = conn.cursor()

    # 新增一個沒有班級的學生
    cursor.execute(
        "INSERT INTO students (name, class_id) VALUES (?, ?)", ("小王", None)
    )
    conn.commit()

    # 查詢所有學生及其班級（包括沒有班級的學生）
    cursor.execute(
        """
        SELECT students.name, classes.class_name
        FROM students
        LEFT JOIN classes ON students.class_id = classes.id
    """
    )

    rows = cursor.fetchall()
    print("所有學生（包括未分配班級）：")
    for row in rows:
        class_name = row[1] if row[1] else "未分配"
        print(f"  {row[0]} - {class_name}")

    conn.close()


def demo_multiple_joins():
    """示範多表連接"""
    print("\n=== 多表連接 ===")

    conn = sqlite3.connect("join_demo.db")
    cursor = conn.cursor()

    # 查詢學生、班級和成績
    cursor.execute(
        """
        SELECT 
            students.name,
            classes.class_name,
            scores.subject,
            scores.score
        FROM students
        INNER JOIN classes ON students.class_id = classes.id
        INNER JOIN scores ON students.id = scores.student_id
        ORDER BY students.name, scores.subject
    """
    )

    rows = cursor.fetchall()
    print("學生完整資訊：")
    for row in rows:
        print(f"  {row[0]} ({row[1]}) - {row[2]}: {row[3]} 分")

    conn.close()


def demo_aggregate_with_join():
    """示範連接後的聚合查詢"""
    print("\n=== 連接後的聚合查詢 ===")

    conn = sqlite3.connect("join_demo.db")
    cursor = conn.cursor()

    # 計算每位學生的平均分數
    cursor.execute(
        """
        SELECT 
            students.name,
            classes.class_name,
            AVG(scores.score) as average,
            COUNT(scores.id) as subject_count
        FROM students
        INNER JOIN classes ON students.class_id = classes.id
        INNER JOIN scores ON students.id = scores.student_id
        GROUP BY students.id
        ORDER BY average DESC
    """
    )

    rows = cursor.fetchall()
    print("學生平均成績排名：")
    for rank, row in enumerate(rows, 1):
        print(
            f"  第 {rank} 名：{row[0]} ({row[1]}) - 平均 {row[2]:.2f} 分（{row[3]} 科）"
        )

    conn.close()


def demo_subquery():
    """示範子查詢"""
    print("\n=== 子查詢 ===")

    conn = sqlite3.connect("join_demo.db")
    cursor = conn.cursor()

    # 查詢成績高於平均分數的記錄
    cursor.execute(
        """
        SELECT 
            students.name,
            scores.subject,
            scores.score
        FROM students
        INNER JOIN scores ON students.id = scores.student_id
        WHERE scores.score > (SELECT AVG(score) FROM scores)
        ORDER BY scores.score DESC
    """
    )

    rows = cursor.fetchall()

    # 先查詢平均分數
    cursor.execute("SELECT AVG(score) FROM scores")
    avg_score = cursor.fetchone()[0]

    print(f"高於平均分數（{avg_score:.2f}）的成績：")
    for row in rows:
        print(f"  {row[0]} - {row[1]}: {row[2]} 分")

    conn.close()


if __name__ == "__main__":
    setup_database()
    demo_inner_join()
    demo_left_join()
    demo_multiple_joins()
    demo_aggregate_with_join()
    demo_subquery()

    print("\n=== 完成 ===")
