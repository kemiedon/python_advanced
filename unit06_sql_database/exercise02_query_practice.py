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
    """
    建立產品資料庫

    TODO: 實作資料庫建立
    - 連接資料庫 products.db
    - 建立 products 資料表
    - 欄位: id, name, category, price, stock, created_at
    """
    pass


def insert_sample_data(conn):
    """
    插入測試資料

    TODO: 實作資料插入
    - 插入至少 10 筆不同分類的產品
    - 包含電子產品、服飾、食品等分類
    - 價格和庫存使用合理的數值
    """
    pass


def query_by_category(conn, category):
    """
    查詢特定分類的產品

    TODO: 實作分類查詢
    - 使用 WHERE 篩選分類
    - 顯示產品名稱和價格
    """
    pass


def query_by_price_range(conn, min_price, max_price):
    """
    查詢價格區間的產品

    TODO: 實作價格區間查詢
    - 使用 WHERE 條件篩選價格範圍
    - 按價格排序顯示
    """
    pass


def query_sorted_by_price(conn, order="ASC"):
    """
    按價格排序查詢

    TODO: 實作排序查詢
    - 使用 ORDER BY 排序
    - 支援升冪（ASC）和降冪（DESC）
    """
    pass


def count_by_category(conn):
    """
    統計每個分類的產品數量

    TODO: 實作分類統計
    - 使用 GROUP BY 和 COUNT()
    - 顯示每個分類和對應的產品數量
    """
    pass


def calculate_average_price(conn):
    """
    計算平均價格

    TODO: 實作平均價格計算
    - 使用 AVG() 函數
    - 整體平均和分類平均
    """
    pass


def find_low_stock_products(conn, threshold=10):
    """
    找出庫存不足的產品

    TODO: 實作庫存查詢
    - 使用 WHERE 篩選庫存
    - 顯示需要補貨的產品
    """
    pass


def main():
    """主程式"""
    print("SQL 查詢練習")
    print("=" * 60)

    # 建立資料庫
    conn = create_database()

    # 插入測試資料
    insert_sample_data(conn)

    # 各種查詢測試
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
