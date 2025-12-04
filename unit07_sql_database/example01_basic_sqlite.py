"""example01_basic_sqlite.py

示範基本 SQLite 資料庫操作
"""

import sqlite3
import os


def demo_create_database():
    """示範建立資料庫"""
    print("=== 示範建立資料庫 ===")

    # 連接資料庫（如果不存在會自動建立）
    conn = sqlite3.connect("students.db")
    print("✓ 資料庫連接成功")

    # 關閉連接
    conn.close()
    print("✓ 資料庫連接已關閉")


def demo_create_table():
    """示範建立資料表"""
    print("\n=== 示範建立資料表 ===")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # 建立學生資料表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    """
    )

    conn.commit()
    print("✓ 資料表 students 建立成功")

    conn.close()


def demo_insert_data():
    """示範插入資料"""
    print("\n=== 示範插入資料 ===")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # 插入單筆資料
    cursor.execute(
        """
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    """,
        ("小明", 20, "三年級"),
    )

    print("✓ 插入了 1 筆資料")

    # 插入多筆資料
    students_data = [
        ("小美", 19, "二年級"),
        ("阿強", 21, "三年級"),
        ("阿花", 20, "二年級"),
    ]

    cursor.executemany(
        """
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    """,
        students_data,
    )

    print(f"✓ 插入了 {len(students_data)} 筆資料")

    conn.commit()
    conn.close()


def demo_query_data():
    """示範查詢資料"""
    print("\n=== 示範查詢資料 ===")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # 查詢所有資料
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print(f"查詢到 {len(rows)} 筆資料：")
    for row in rows:
        print(f"  ID: {row[0]}, 姓名: {row[1]}, 年齡: {row[2]}, 年級: {row[3]}")

    conn.close()


def demo_query_with_condition():
    """示範條件查詢"""
    print("\n=== 示範條件查詢 ===")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # 查詢三年級的學生
    cursor.execute(
        """
        SELECT * FROM students
        WHERE grade = ?
    """,
        ("三年級",),
    )

    rows = cursor.fetchall()

    print("三年級的學生：")
    for row in rows:
        print(f"  {row[1]} ({row[2]} 歲)")

    conn.close()


def demo_update_data():
    """示範更新資料"""
    print("\n=== 示範更新資料 ===")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # 更新小明的年齡
    cursor.execute(
        """
        UPDATE students
        SET age = ?
        WHERE name = ?
    """,
        (21, "小明"),
    )

    print(f"✓ 更新了 {cursor.rowcount} 筆資料")

    conn.commit()
    conn.close()


def demo_delete_data():
    """示範刪除資料"""
    print("\n=== 示範刪除資料 ===")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # 先查詢資料數量
    cursor.execute("SELECT COUNT(*) FROM students")
    before_count = cursor.fetchone()[0]
    print(f"刪除前：{before_count} 筆資料")

    # 刪除年齡大於 20 的學生（示範，實際不執行）
    # cursor.execute("DELETE FROM students WHERE age > ?", (20,))
    # conn.commit()

    print("（為保留資料，此次不執行刪除操作）")

    conn.close()


def demo_drop_table():
    """示範刪除資料表"""
    print("\n=== 示範刪除資料表 ===")

    # 建立一個測試用的表
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS temp_table (
            id INTEGER PRIMARY KEY,
            data TEXT
        )
    """
    )
    conn.commit()
    print("✓ 建立測試表 temp_table")

    # 刪除測試表
    cursor.execute("DROP TABLE IF EXISTS temp_table")
    conn.commit()
    print("✓ 刪除測試表 temp_table")

    conn.close()


if __name__ == "__main__":
    # 清除舊的資料庫檔案（重新開始）
    if os.path.exists("students.db"):
        os.remove("students.db")
        print("已刪除舊的資料庫檔案\n")

    demo_create_database()
    demo_create_table()
    demo_insert_data()
    demo_query_data()
    demo_query_with_condition()
    demo_update_data()
    demo_delete_data()
    demo_drop_table()

    print("\n=== 完成 ===")
