"""
練習 4：圖書館借閱系統 ⭐⭐⭐⭐

任務：
建立完整的圖書館借閱管理系統，包含書籍、會員、借閱記錄等。

要求：
1. 建立資料表：
   - books: 書籍資料（ISBN、書名、作者、分類、庫存）
   - members: 會員資料（會員編號、姓名、電話、加入日期）
   - borrowings: 借閱記錄（借閱編號、會員編號、ISBN、借閱日期、歸還日期）
2. 實作功能：
   - 書籍管理（新增、查詢、更新庫存）
   - 會員管理（新增、查詢）
   - 借書（檢查庫存、建立記錄、更新庫存）
   - 還書（更新記錄、恢復庫存）
   - 查詢會員的借閱記錄
   - 查詢逾期未還的書籍（借閱超過 14 天）
   - 統計熱門書籍（借閱次數最多）
3. 使用交易處理確保資料一致性

提示：
- 借書和還書需要同時更新多個資料表
- 使用 transaction 確保資料完整性
- 日期比較使用 julianday() 函數
"""

import sqlite3
from datetime import datetime, timedelta


class LibrarySystem:
    """圖書館管理系統"""

    def __init__(self, db_name="library.db"):
        """初始化圖書館系統"""
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        """建立資料表"""
        cursor = self.conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS borrowings")
        cursor.execute("DROP TABLE IF EXISTS books")
        cursor.execute("DROP TABLE IF EXISTS members")

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                isbn TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 0
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS members (
                member_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT,
                joined_at TEXT NOT NULL
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id TEXT NOT NULL,
                isbn TEXT NOT NULL,
                borrowed_at TEXT NOT NULL,
                returned_at TEXT,
                FOREIGN KEY (member_id) REFERENCES members(member_id),
                FOREIGN KEY (isbn) REFERENCES books(isbn)
            )
        """
        )
        self.conn.commit()

    def add_book(self, isbn, title, author, category, quantity):
        """新增書籍"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO books (isbn, title, author, category, quantity) VALUES (?, ?, ?, ?, ?)",
            (isbn, title, author, category, quantity),
        )
        self.conn.commit()
        print(f"  ✓ 新增書籍：《{title}》（庫存 {quantity} 本）")

    def add_member(self, member_id, name, phone):
        """新增會員"""
        cursor = self.conn.cursor()
        joined_at = datetime.now().strftime("%Y-%m-%d")
        cursor.execute(
            "INSERT OR REPLACE INTO members (member_id, name, phone, joined_at) VALUES (?, ?, ?, ?)",
            (member_id, name, phone, joined_at),
        )
        self.conn.commit()
        print(f"  ✓ 新增會員：{name}（{member_id}）")

    def borrow_book(self, member_id, isbn):
        """借書"""
        cursor = self.conn.cursor()

        # 確認會員存在
        cursor.execute("SELECT name FROM members WHERE member_id = ?", (member_id,))
        member = cursor.fetchone()
        if not member:
            print(f"  ✗ 會員 {member_id} 不存在")
            return False

        # 確認書籍存在且有庫存
        cursor.execute("SELECT title, quantity FROM books WHERE isbn = ?", (isbn,))
        book = cursor.fetchone()
        if not book:
            print(f"  ✗ ISBN {isbn} 不存在")
            return False
        if book[1] <= 0:
            print(f"  ✗ 《{book[0]}》已無庫存可借")
            return False

        try:
            borrowed_at = datetime.now().strftime("%Y-%m-%d")
            cursor.execute(
                "INSERT INTO borrowings (member_id, isbn, borrowed_at) VALUES (?, ?, ?)",
                (member_id, isbn, borrowed_at),
            )
            cursor.execute(
                "UPDATE books SET quantity = quantity - 1 WHERE isbn = ?", (isbn,)
            )
            self.conn.commit()
            print(f"  ✓ {member[0]} 借閱《{book[0]}》成功（借閱日期：{borrowed_at}）")
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"  ✗ 借書失敗：{e}")
            return False

    def return_book(self, borrowing_id):
        """還書"""
        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT b.isbn, bk.title, b.returned_at FROM borrowings b JOIN books bk ON b.isbn = bk.isbn WHERE b.id = ?",
            (borrowing_id,),
        )
        record = cursor.fetchone()
        if not record:
            print(f"  ✗ 借閱記錄 {borrowing_id} 不存在")
            return False
        if record[2]:
            print(f"  ✗ 《{record[1]}》已於 {record[2]} 歸還")
            return False

        try:
            returned_at = datetime.now().strftime("%Y-%m-%d")
            cursor.execute(
                "UPDATE borrowings SET returned_at = ? WHERE id = ?",
                (returned_at, borrowing_id),
            )
            cursor.execute(
                "UPDATE books SET quantity = quantity + 1 WHERE isbn = ?", (record[0],)
            )
            self.conn.commit()
            print(f"  ✓ 《{record[1]}》歸還成功（歸還日期：{returned_at}）")
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"  ✗ 還書失敗：{e}")
            return False

    def get_member_borrowings(self, member_id):
        """查詢會員的借閱記錄"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT br.id, bk.title, br.borrowed_at, br.returned_at
            FROM borrowings br
            JOIN books bk ON br.isbn = bk.isbn
            WHERE br.member_id = ?
            ORDER BY br.borrowed_at DESC
        """,
            (member_id,),
        )
        rows = cursor.fetchall()
        if not rows:
            print(f"  查無會員 {member_id} 的借閱記錄")
            return
        print(f"  {'ID':<5} {'書名':<25} {'借閱日期':<12} {'歸還日期':<12}")
        print(f"  {'-'*56}")
        for rid, title, borrowed_at, returned_at in rows:
            status = returned_at if returned_at else "未歸還"
            print(f"  {rid:<5} {title:<25} {borrowed_at:<12} {status:<12}")

    def find_overdue_books(self, days=14):
        """查詢逾期未還的書籍"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT br.id, m.name, bk.title, br.borrowed_at,
                   CAST(julianday('now') - julianday(br.borrowed_at) AS INTEGER) AS overdue_days
            FROM borrowings br
            JOIN members m ON br.member_id = m.member_id
            JOIN books bk ON br.isbn = bk.isbn
            WHERE br.returned_at IS NULL
              AND julianday('now') - julianday(br.borrowed_at) > ?
            ORDER BY overdue_days DESC
        """,
            (days,),
        )
        rows = cursor.fetchall()
        if not rows:
            print(f"  目前沒有逾期（超過 {days} 天）未還的書籍")
            return
        print(f"  {'ID':<5} {'會員':<10} {'書名':<25} {'借閱日期':<12} {'逾期天數':>8}")
        print(f"  {'-'*62}")
        for rid, name, title, borrowed_at, overdue_days in rows:
            print(f"  {rid:<5} {name:<10} {title:<25} {borrowed_at:<12} {overdue_days:>8} 天")

    def get_popular_books(self, limit=5):
        """統計熱門書籍"""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT bk.title, bk.author, COUNT(br.id) AS borrow_count
            FROM books bk
            LEFT JOIN borrowings br ON bk.isbn = br.isbn
            GROUP BY bk.isbn
            ORDER BY borrow_count DESC
            LIMIT ?
        """,
            (limit,),
        )
        rows = cursor.fetchall()
        print(f"  {'書名':<25} {'作者':<15} {'借閱次數':>8}")
        print(f"  {'-'*50}")
        for title, author, count in rows:
            print(f"  {title:<25} {author:<15} {count:>8} 次")

    def get_available_books(self):
        """查詢可借閱的書籍"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT title, author, category, quantity FROM books WHERE quantity > 0 ORDER BY category, title"
        )
        rows = cursor.fetchall()
        if not rows:
            print("  目前所有書籍已借完")
            return
        print(f"  {'書名':<25} {'作者':<15} {'分類':<12} {'庫存':>6}")
        print(f"  {'-'*60}")
        for title, author, category, quantity in rows:
            print(f"  {title:<25} {author:<15} {category:<12} {quantity:>6} 本")

    def close(self):
        """關閉資料庫連接"""
        self.conn.close()


def main():
    """主程式"""
    print("圖書館借閱系統")
    print("=" * 60)

    library = LibrarySystem()

    print("\n【新增書籍】")
    library.add_book("978-1234567890", "Python 程式設計", "王小明", "程式設計", 5)
    library.add_book("978-2345678901", "資料科學入門", "李小華", "資料科學", 3)
    library.add_book("978-3456789012", "SQL 資料庫", "張大同", "資料庫", 4)

    print("\n【新增會員】")
    library.add_member("M001", "陳小美", "0912-345-678")
    library.add_member("M002", "林大強", "0923-456-789")

    print("\n【借書】")
    library.borrow_book("M001", "978-1234567890")
    library.borrow_book("M001", "978-2345678901")
    library.borrow_book("M002", "978-1234567890")

    print("\n【可借閱書籍】")
    library.get_available_books()

    print("\n【陳小美的借閱記錄】")
    library.get_member_borrowings("M001")

    print("\n【還書】")
    library.return_book(1)

    print("\n【逾期書籍】")
    library.find_overdue_books()

    print("\n【熱門書籍】")
    library.get_popular_books()

    library.close()


if __name__ == "__main__":
    main()
