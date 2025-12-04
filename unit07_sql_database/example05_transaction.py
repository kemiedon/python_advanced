"""example05_transaction.py

示範交易處理與錯誤回復
"""

import sqlite3


def demo_transaction_basic():
    """示範基本交易處理"""
    print("=== 基本交易處理 ===")

    conn = sqlite3.connect("transaction_demo.db")
    cursor = conn.cursor()

    # 建立帳戶表
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance INTEGER
        )
    """
    )

    cursor.execute("DELETE FROM accounts")

    # 插入測試資料
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("小明", 1000))
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("小美", 500))
    conn.commit()

    print("初始帳戶餘額：")
    cursor.execute("SELECT name, balance FROM accounts")
    for row in cursor.fetchall():
        print(f"  {row[0]}: ${row[1]}")

    conn.close()


def demo_transaction_commit():
    """示範交易提交"""
    print("\n=== 交易提交（轉帳成功）===")

    conn = sqlite3.connect("transaction_demo.db")
    cursor = conn.cursor()

    try:
        # 開始交易
        cursor.execute("BEGIN TRANSACTION")

        # 小明轉帳 300 元給小美
        cursor.execute(
            "UPDATE accounts SET balance = balance - 300 WHERE name = ?", ("小明",)
        )
        cursor.execute(
            "UPDATE accounts SET balance = balance + 300 WHERE name = ?", ("小美",)
        )

        # 提交交易
        conn.commit()
        print("✓ 轉帳成功")

    except Exception as e:
        conn.rollback()
        print(f"✗ 轉帳失敗：{e}")

    # 顯示結果
    cursor.execute("SELECT name, balance FROM accounts")
    print("轉帳後帳戶餘額：")
    for row in cursor.fetchall():
        print(f"  {row[0]}: ${row[1]}")

    conn.close()


def demo_transaction_rollback():
    """示範交易回滾"""
    print("\n=== 交易回滾（轉帳失敗）===")

    conn = sqlite3.connect("transaction_demo.db")
    cursor = conn.cursor()

    # 先顯示轉帳前餘額
    cursor.execute("SELECT name, balance FROM accounts")
    print("轉帳前帳戶餘額：")
    before_balances = cursor.fetchall()
    for row in before_balances:
        print(f"  {row[0]}: ${row[1]}")

    try:
        # 開始交易
        cursor.execute("BEGIN TRANSACTION")

        # 小明轉帳 1000 元給小美（但小明餘額不足）
        cursor.execute(
            "UPDATE accounts SET balance = balance - 1000 WHERE name = ?", ("小明",)
        )

        # 檢查餘額是否為負
        cursor.execute("SELECT balance FROM accounts WHERE name = ?", ("小明",))
        balance = cursor.fetchone()[0]

        if balance < 0:
            raise Exception("餘額不足")

        cursor.execute(
            "UPDATE accounts SET balance = balance + 1000 WHERE name = ?", ("小美",)
        )

        # 提交交易
        conn.commit()
        print("✓ 轉帳成功")

    except Exception as e:
        conn.rollback()
        print(f"✗ 轉帳失敗：{e}")
        print("✓ 交易已回滾")

    # 顯示結果（應該與轉帳前相同）
    cursor.execute("SELECT name, balance FROM accounts")
    print("回滾後帳戶餘額（應與轉帳前相同）：")
    for row in cursor.fetchall():
        print(f"  {row[0]}: ${row[1]}")

    conn.close()


def demo_context_manager():
    """示範使用 with 語句自動管理交易"""
    print("\n=== 使用 with 自動管理交易 ===")

    conn = sqlite3.connect("transaction_demo.db")

    try:
        with conn:
            cursor = conn.cursor()

            # 小明轉帳 100 元給小美
            cursor.execute(
                "UPDATE accounts SET balance = balance - 100 WHERE name = ?", ("小明",)
            )
            cursor.execute(
                "UPDATE accounts SET balance = balance + 100 WHERE name = ?", ("小美",)
            )

        print("✓ 轉帳成功（自動提交）")

    except Exception as e:
        print(f"✗ 轉帳失敗：{e}（自動回滾）")

    # 顯示結果
    cursor = conn.cursor()
    cursor.execute("SELECT name, balance FROM accounts")
    print("最終帳戶餘額：")
    for row in cursor.fetchall():
        print(f"  {row[0]}: ${row[1]}")

    conn.close()


if __name__ == "__main__":
    demo_transaction_basic()
    demo_transaction_commit()
    demo_transaction_rollback()
    demo_context_manager()

    print("\n=== 完成 ===")
