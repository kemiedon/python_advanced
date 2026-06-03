"""
練習 2：查詢練習 ⭐⭐

任務：
使用 SQLite 進行各種查詢操作。

要求：
1. 建立產品資料表（產品名稱、分類、價格、庫存、上架日期）
2. 插入至少 10 筆測試資料
3. 實作以下查詢功能：
   - 查詢特定分類的產品
   - 查詢價格區間的產品
   - 按價格排序
   - 統計每個分類的產品數量
   - 計算平均價格
   - 找出庫存不足（< 10）的產品

提示：
- 使用 WHERE 子句篩選
- 使用 ORDER BY 排序
- 使用 GROUP BY 和聚合函數統計
"""

import sqlite3
from datetime import datetime, timedelta
import random


def create_database():
    """建立產品資料庫"""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """
    )
    conn.commit()
    print("✓ 資料庫建立成功")
    return conn


def insert_sample_data(conn):
    """插入測試資料"""
    cursor = conn.cursor()

    today = datetime.now()
    products = [
        ("iPhone 15", "電子產品", 29900, 15, (today - timedelta(days=10)).strftime("%Y-%m-%d")),
        ("MacBook Pro", "電子產品", 59900, 8, (today - timedelta(days=20)).strftime("%Y-%m-%d")),
        ("AirPods", "電子產品", 5990, 5, (today - timedelta(days=5)).strftime("%Y-%m-%d")),
        ("T恤", "服飾", 490, 50, (today - timedelta(days=3)).strftime("%Y-%m-%d")),
        ("牛仔褲", "服飾", 1290, 30, (today - timedelta(days=7)).strftime("%Y-%m-%d")),
        ("運動外套", "服飾", 2490, 20, (today - timedelta(days=15)).strftime("%Y-%m-%d")),
        ("蘋果", "食品", 120, 100, today.strftime("%Y-%m-%d")),
        ("巧克力", "食品", 89, 200, today.strftime("%Y-%m-%d")),
        ("礦泉水", "食品", 25, 3, (today - timedelta(days=1)).strftime("%Y-%m-%d")),
        ("Python 入門書", "書籍", 650, 25, (today - timedelta(days=30)).strftime("%Y-%m-%d")),
        ("資料庫設計", "書籍", 780, 7, (today - timedelta(days=12)).strftime("%Y-%m-%d")),
    ]

    cursor.executemany(
        "INSERT INTO products (name, category, price, stock, created_at) VALUES (?, ?, ?, ?, ?)",
        products,
    )
    conn.commit()
    print(f"✓ 成功插入 {len(products)} 筆產品資料")


def query_by_category(conn, category):
    """查詢特定分類的產品"""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, price FROM products WHERE category = ? ORDER BY price",
        (category,),
    )
    rows = cursor.fetchall()
    if not rows:
        print(f"  查無「{category}」分類的產品")
        return
    print(f"  {'產品名稱':<20} {'價格':>10}")
    print(f"  {'-'*32}")
    for name, price in rows:
        print(f"  {name:<20} {price:>10,.0f}")


def query_by_price_range(conn, min_price, max_price):
    """查詢價格區間的產品"""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, category, price FROM products WHERE price BETWEEN ? AND ? ORDER BY price",
        (min_price, max_price),
    )
    rows = cursor.fetchall()
    if not rows:
        print(f"  查無價格 {min_price}~{max_price} 的產品")
        return
    print(f"  {'產品名稱':<20} {'分類':<12} {'價格':>10}")
    print(f"  {'-'*44}")
    for name, category, price in rows:
        print(f"  {name:<20} {category:<12} {price:>10,.0f}")


def query_sorted_by_price(conn, order="ASC"):
    """按價格排序查詢"""
    cursor = conn.cursor()
    cursor.execute(f"SELECT name, category, price FROM products ORDER BY price {order}")
    rows = cursor.fetchall()
    print(f"  {'產品名稱':<20} {'分類':<12} {'價格':>10}")
    print(f"  {'-'*44}")
    for name, category, price in rows:
        print(f"  {name:<20} {category:<12} {price:>10,.0f}")


def count_by_category(conn):
    """統計每個分類的產品數量"""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT category, COUNT(*) AS count FROM products GROUP BY category ORDER BY count DESC"
    )
    rows = cursor.fetchall()
    print(f"  {'分類':<15} {'產品數量':>8}")
    print(f"  {'-'*24}")
    for category, count in rows:
        print(f"  {category:<15} {count:>8}")


def calculate_average_price(conn):
    """計算平均價格"""
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(price) FROM products")
    overall_avg = cursor.fetchone()[0]
    print(f"  整體平均價格: {overall_avg:,.2f}")

    cursor.execute(
        "SELECT category, AVG(price) AS avg_price FROM products GROUP BY category ORDER BY avg_price DESC"
    )
    rows = cursor.fetchall()
    print(f"\n  {'分類':<15} {'平均價格':>12}")
    print(f"  {'-'*28}")
    for category, avg in rows:
        print(f"  {category:<15} {avg:>12,.2f}")


def find_low_stock_products(conn, threshold=10):
    """找出庫存不足的產品"""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, category, stock FROM products WHERE stock < ? ORDER BY stock",
        (threshold,),
    )
    rows = cursor.fetchall()
    if not rows:
        print(f"  目前沒有庫存低於 {threshold} 的產品")
        return
    print(f"  {'產品名稱':<20} {'分類':<12} {'庫存':>6}")
    print(f"  {'-'*40}")
    for name, category, stock in rows:
        print(f"  {name:<20} {category:<12} {stock:>6}  ⚠️ 需補貨")


def main():
    """主程式"""
    print("SQL 查詢練習")
    print("=" * 60)

    conn = create_database()
    insert_sample_data(conn)

    print("\n【查詢「電子產品」分類】")
    query_by_category(conn, "電子產品")

    print("\n【查詢價格 1000-5000 的產品】")
    query_by_price_range(conn, 1000, 5000)

    print("\n【按價格由高到低排序】")
    query_sorted_by_price(conn, "DESC")

    print("\n【統計每個分類的產品數量】")
    count_by_category(conn)

    print("\n【計算平均價格】")
    calculate_average_price(conn)

    print("\n【查詢庫存不足的產品】")
    find_low_stock_products(conn)

    conn.close()


if __name__ == "__main__":
    main()
