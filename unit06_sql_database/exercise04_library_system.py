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
        """
        初始化圖書館系統

        TODO: 實作初始化
        - 連接資料庫
        - 建立資料表
        """
        pass

    def create_tables(self):
        """
        建立資料表

        TODO: 實作資料表建立
        - books 表
        - members 表
        - borrowings 表（外鍵關聯）
        """
        pass

    def add_book(self, isbn, title, author, category, quantity):
        """
        新增書籍

        TODO: 實作新增書籍
        """
        pass

    def add_member(self, member_id, name, phone):
        """
        新增會員

        TODO: 實作新增會員
        - 記錄加入日期
        """
        pass

    def borrow_book(self, member_id, isbn):
        """
        借書

        TODO: 實作借書邏輯
        - 檢查書籍庫存
        - 檢查會員是否存在
        - 使用 transaction：
          1. 新增借閱記錄
          2. 減少書籍庫存
        - 記錄借閱日期
        """
        pass

    def return_book(self, borrowing_id):
        """
        還書

        TODO: 實作還書邏輯
        - 使用 transaction：
          1. 更新借閱記錄的歸還日期
          2. 增加書籍庫存
        """
        pass

    def get_member_borrowings(self, member_id):
        """
        查詢會員的借閱記錄

        TODO: 實作借閱記錄查詢
        - JOIN books 表顯示書名
        - 顯示借閱日期和歸還狀態
        """
        pass

    def find_overdue_books(self, days=14):
        """
        查詢逾期未還的書籍

        TODO: 實作逾期查詢
        - 找出未歸還且超過指定天數的借閱
        - 使用 julianday() 計算日期差
        """
        pass

    def get_popular_books(self, limit=5):
        """
        統計熱門書籍

        TODO: 實作熱門書籍統計
        - 計算每本書的借閱次數
        - 按借閱次數排序
        """
        pass

    def get_available_books(self):
        """
        查詢可借閱的書籍

        TODO: 實作可借書籍查詢
        - 庫存 > 0 的書籍
        """
        pass

    def close(self):
        """關閉資料庫連接"""
        pass


def main():
    """主程式"""
    print("圖書館借閱系統")
    print("=" * 60)

    # 建立系統
    library = LibrarySystem()

    # 新增書籍
    print("\n【新增書籍】")
    library.add_book("978-1234567890", "Python 程式設計", "王小明", "程式設計", 5)
    library.add_book("978-2345678901", "資料科學入門", "李小華", "資料科學", 3)
    library.add_book("978-3456789012", "SQL 資料庫", "張大同", "資料庫", 4)

    # 新增會員
    print("\n【新增會員】")
    library.add_member("M001", "陳小美", "0912-345-678")
    library.add_member("M002", "林大強", "0923-456-789")

    # 借書
    print("\n【借書】")
    library.borrow_book("M001", "978-1234567890")
    library.borrow_book("M001", "978-2345678901")
    library.borrow_book("M002", "978-1234567890")

    # 查詢可借書籍
    print("\n【可借閱書籍】")
    library.get_available_books()

    # 查詢會員借閱記錄
    print("\n【陳小美的借閱記錄】")
    library.get_member_borrowings("M001")

    # 還書
    print("\n【還書】")
    library.return_book(1)

    # 查詢逾期書籍
    print("\n【逾期書籍】")
    library.find_overdue_books()

    # 熱門書籍
    print("\n【熱門書籍】")
    library.get_popular_books()

    library.close()


if __name__ == "__main__":
    main()
