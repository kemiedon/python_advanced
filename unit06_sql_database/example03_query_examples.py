"""example03_query_examples.py

示範各種 SQL 查詢範例
"""

import sqlite3


def setup_database():
    """建立測試資料庫"""
    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 建立資料表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT,
            score INTEGER
        )
    """
    )

    # 清空舊資料
    cursor.execute("DELETE FROM students")

    # 插入測試資料
    students = [
        ("小明", 20, "三年級", 85),
        ("小美", 19, "二年級", 92),
        ("阿強", 21, "三年級", 78),
        ("阿花", 20, "二年級", 88),
        ("小華", 22, "三年級", 95),
        ("小李", 19, "一年級", 82),
        ("大衛", 21, "二年級", 90),
        ("瑪麗", 20, "三年級", 87),
    ]

    cursor.executemany(
        """
        INSERT INTO students (name, age, grade, score)
        VALUES (?, ?, ?, ?)
    """,
        students,
    )

    conn.commit()
    conn.close()
    print("✓ 測試資料已建立")


def demo_select_all():
    """示範查詢所有資料"""
    print("\n=== 查詢所有學生 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[1]} - {row[3]} - {row[4]} 分")

    conn.close()


def demo_select_columns():
    """示範查詢特定欄位"""
    print("\n=== 查詢特定欄位 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, score FROM students")
    rows = cursor.fetchall()

    print("學生成績：")
    for row in rows:
        print(f"  {row[0]}: {row[1]} 分")

    conn.close()


def demo_where_clause():
    """示範 WHERE 條件查詢"""
    print("\n=== WHERE 條件查詢 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 查詢成績大於 85 的學生
    cursor.execute(
        """
        SELECT name, score
        FROM students
        WHERE score > 85
    """
    )

    rows = cursor.fetchall()
    print("成績大於 85 分的學生：")
    for row in rows:
        print(f"  {row[0]}: {row[1]} 分")

    conn.close()


def demo_order_by():
    """示範排序查詢"""
    print("\n=== ORDER BY 排序 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 依成績由高到低排序
    cursor.execute(
        """
        SELECT name, score
        FROM students
        ORDER BY score DESC
    """
    )

    rows = cursor.fetchall()
    print("成績排名（由高到低）：")
    for rank, row in enumerate(rows, 1):
        print(f"  第 {rank} 名：{row[0]} ({row[1]} 分)")

    conn.close()


def demo_limit():
    """示範 LIMIT 限制筆數"""
    print("\n=== LIMIT 限制筆數 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 查詢前 3 名
    cursor.execute(
        """
        SELECT name, score
        FROM students
        ORDER BY score DESC
        LIMIT 3
    """
    )

    rows = cursor.fetchall()
    print("前 3 名：")
    for rank, row in enumerate(rows, 1):
        print(f"  第 {rank} 名：{row[0]} ({row[1]} 分)")

    conn.close()


def demo_aggregate_functions():
    """示範聚合函數"""
    print("\n=== 聚合函數（統計）===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 計算各種統計數據
    cursor.execute(
        """
        SELECT 
            COUNT(*) as total,
            AVG(score) as average,
            MAX(score) as highest,
            MIN(score) as lowest,
            SUM(score) as sum
        FROM students
    """
    )

    row = cursor.fetchone()
    print(f"總人數：{row[0]}")
    print(f"平均分數：{row[1]:.2f}")
    print(f"最高分：{row[2]}")
    print(f"最低分：{row[3]}")
    print(f"總分：{row[4]}")

    conn.close()


def demo_group_by():
    """示範 GROUP BY 分組"""
    print("\n=== GROUP BY 分組統計 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 依年級分組統計
    cursor.execute(
        """
        SELECT 
            grade,
            COUNT(*) as count,
            AVG(score) as average
        FROM students
        GROUP BY grade
        ORDER BY grade
    """
    )

    rows = cursor.fetchall()
    print("各年級統計：")
    for row in rows:
        print(f"  {row[0]}: {row[1]} 人，平均 {row[2]:.2f} 分")

    conn.close()


def demo_having():
    """示範 HAVING 條件"""
    print("\n=== HAVING 分組後篩選 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 查詢平均分數大於 85 的年級
    cursor.execute(
        """
        SELECT 
            grade,
            AVG(score) as average
        FROM students
        GROUP BY grade
        HAVING AVG(score) > 85
    """
    )

    rows = cursor.fetchall()
    print("平均分數大於 85 的年級：")
    for row in rows:
        print(f"  {row[0]}: 平均 {row[1]:.2f} 分")

    conn.close()


def demo_like_pattern():
    """示範 LIKE 模糊查詢"""
    print("\n=== LIKE 模糊查詢 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 查詢名字中包含「小」的學生
    cursor.execute(
        """
        SELECT name, score
        FROM students
        WHERE name LIKE ?
    """,
        ("%小%",),
    )

    rows = cursor.fetchall()
    print("名字中包含「小」的學生：")
    for row in rows:
        print(f"  {row[0]}: {row[1]} 分")

    conn.close()


def demo_in_operator():
    """示範 IN 運算子"""
    print("\n=== IN 運算子 ===")

    conn = sqlite3.connect("query_demo.db")
    cursor = conn.cursor()

    # 查詢二年級或三年級的學生
    cursor.execute(
        """
        SELECT name, grade, score
        FROM students
        WHERE grade IN (?, ?)
        ORDER BY grade, score DESC
    """,
        ("二年級", "三年級"),
    )

    rows = cursor.fetchall()
    print("二年級和三年級的學生：")
    for row in rows:
        print(f"  {row[0]} ({row[1]}): {row[2]} 分")

    conn.close()


if __name__ == "__main__":
    setup_database()
    demo_select_all()
    demo_select_columns()
    demo_where_clause()
    demo_order_by()
    demo_limit()
    demo_aggregate_functions()
    demo_group_by()
    demo_having()
    demo_like_pattern()
    demo_in_operator()

    print("\n=== 完成 ===")
