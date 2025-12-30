"""exercise01_create_database.py

練習 1：建立學生資料庫（難度：⭐）

任務：
1. 建立一個名為 school.db 的資料庫
2. 建立 students 資料表，包含：id、student_id、name、age、major
3. 插入至少 5 筆學生資料
4. 查詢並顯示所有學生資料
"""

import sqlite3


def create_database():
    """建立資料庫和資料表"""
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # 建立學生資料表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT
        )
    """
    )

    conn.commit()
    print("✓ 資料庫和資料表建立成功")
    conn.close()


def insert_students():
    """插入學生資料"""
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    students = [
        ("S001", "小明", 20, "資訊工程"),
        ("S002", "小美", 19, "企業管理"),
        ("S003", "阿強", 21, "電機工程"),
        ("S004", "阿花", 20, "會計"),
        ("S005", "小華", 22, "資訊工程"),
    ]

    # 清空舊資料
    cursor.execute("DELETE FROM students")

    cursor.executemany(
        """
        INSERT INTO students (student_id, name, age, major)
        VALUES (?, ?, ?, ?)
    """,
        students,
    )

    conn.commit()
    print(f"✓ 成功插入 {len(students)} 筆學生資料")
    conn.close()


def display_all_students():
    """顯示所有學生資料"""
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print(f"\n{'ID':<5} {'學號':<10} {'姓名':<10} {'年齡':<6} {'科系':<15}")
    print("-" * 50)

    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<10} {row[3]:<6} {row[4]:<15}")

    conn.close()


if __name__ == "__main__":
    print("=== 練習 1：建立學生資料庫 ===\n")

    create_database()
    insert_students()
    display_all_students()

    print("\n=== 完成 ===")
