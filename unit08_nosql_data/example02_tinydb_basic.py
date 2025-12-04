"""
範例 2：TinyDB 基本操作

這個範例介紹 TinyDB 這個輕量級的 NoSQL 資料庫，
展示基本的 CRUD 操作（Create, Read, Update, Delete）。

生活情境：
管理圖書館的藏書資料，包含書名、作者、ISBN、庫存數量等。

注意：需要先安裝 TinyDB
pip install tinydb
"""

from tinydb import TinyDB, Query


def create_sample_database():
    """建立範例資料庫"""
    print("【建立資料庫】")

    # 建立 TinyDB 資料庫
    db = TinyDB("library.json", indent=2, ensure_ascii=False)

    # 清空資料表（重新開始）
    db.truncate()

    print(f"✓ 已建立資料庫：library.json")
    return db


def insert_books(db):
    """新增書籍資料"""
    print("\n【新增書籍】")

    books = [
        {
            "title": "Python 程式設計入門",
            "author": "王小明",
            "isbn": "978-1234567890",
            "quantity": 5,
            "category": "程式設計",
        },
        {
            "title": "資料科學基礎",
            "author": "李小華",
            "isbn": "978-2345678901",
            "quantity": 3,
            "category": "資料科學",
        },
        {
            "title": "JavaScript 實戰",
            "author": "張大同",
            "isbn": "978-3456789012",
            "quantity": 7,
            "category": "程式設計",
        },
        {
            "title": "機器學習導論",
            "author": "陳小美",
            "isbn": "978-4567890123",
            "quantity": 2,
            "category": "人工智慧",
        },
        {
            "title": "Web 開發完全指南",
            "author": "林大強",
            "isbn": "978-5678901234",
            "quantity": 4,
            "category": "程式設計",
        },
    ]

    # 插入多筆資料
    doc_ids = db.insert_multiple(books)
    print(f"✓ 已新增 {len(doc_ids)} 本書籍")

    # 新增單筆資料
    doc_id = db.insert(
        {
            "title": "SQL 資料庫設計",
            "author": "黃小芳",
            "isbn": "978-6789012345",
            "quantity": 6,
            "category": "資料庫",
        }
    )
    print(f"✓ 已新增書籍 (文件 ID: {doc_id})")


def read_all_books(db):
    """讀取所有書籍"""
    print("\n【所有書籍】")

    all_books = db.all()

    print(f"共有 {len(all_books)} 本書籍：")
    print("-" * 80)

    for book in all_books:
        print(f"ID: {book.doc_id}")
        print(f"書名: {book['title']}")
        print(f"作者: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"庫存: {book['quantity']} 本")
        print(f"分類: {book['category']}")
        print("-" * 80)


def search_books(db):
    """搜尋書籍"""
    print("\n【搜尋書籍】")

    # 建立查詢物件
    Book = Query()

    # 查詢：分類為「程式設計」的書籍
    print("\n1. 分類為「程式設計」的書籍：")
    results = db.search(Book.category == "程式設計")
    for book in results:
        print(f"  - {book['title']} ({book['author']})")

    # 查詢：庫存大於 4 本的書籍
    print("\n2. 庫存大於 4 本的書籍：")
    results = db.search(Book.quantity > 4)
    for book in results:
        print(f"  - {book['title']} (庫存: {book['quantity']} 本)")

    # 查詢：書名包含「Python」的書籍
    print("\n3. 書名包含「Python」的書籍：")
    results = db.search(Book.title.matches(".*Python.*"))
    for book in results:
        print(f"  - {book['title']}")

    # 查詢：作者為「王小明」或「李小華」的書籍
    print("\n4. 作者為「王小明」或「李小華」的書籍：")
    results = db.search((Book.author == "王小明") | (Book.author == "李小華"))
    for book in results:
        print(f"  - {book['title']} (作者: {book['author']})")


def update_books(db):
    """更新書籍資料"""
    print("\n【更新書籍】")

    Book = Query()

    # 更新：將「Python 程式設計入門」的庫存增加 3 本
    print("\n1. 更新「Python 程式設計入門」的庫存")
    book = db.get(Book.title == "Python 程式設計入門")
    if book:
        new_quantity = book["quantity"] + 3
        db.update({"quantity": new_quantity}, Book.title == "Python 程式設計入門")
        print(f"  原庫存: {book['quantity']} 本")
        print(f"  新庫存: {new_quantity} 本")

    # 更新：將所有「程式設計」分類的書籍庫存減 1
    print("\n2. 將所有「程式設計」分類的書籍庫存減 1")
    books = db.search(Book.category == "程式設計")
    print(f"  影響 {len(books)} 本書籍")

    def decrease_quantity(fields):
        fields["quantity"] = max(0, fields["quantity"] - 1)
        return fields

    db.update(decrease_quantity, Book.category == "程式設計")


def delete_books(db):
    """刪除書籍"""
    print("\n【刪除書籍】")

    Book = Query()

    # 刪除：庫存為 0 的書籍
    print("\n1. 刪除庫存為 0 的書籍")
    count = len(db.search(Book.quantity == 0))
    if count > 0:
        db.remove(Book.quantity == 0)
        print(f"  ✓ 已刪除 {count} 本書籍")
    else:
        print("  目前沒有庫存為 0 的書籍")

    # 刪除：特定 ISBN 的書籍
    print("\n2. 刪除 ISBN 為 978-4567890123 的書籍")
    book = db.get(Book.isbn == "978-4567890123")
    if book:
        db.remove(Book.isbn == "978-4567890123")
        print(f"  ✓ 已刪除：{book['title']}")


def main():
    """主程式"""
    print("TinyDB 基本操作範例：圖書館藏書管理")
    print("=" * 80)

    # 建立資料庫
    db = create_sample_database()

    # 新增書籍
    insert_books(db)

    # 讀取所有書籍
    read_all_books(db)

    # 搜尋書籍
    search_books(db)

    # 更新書籍
    update_books(db)

    # 顯示更新後的資料
    print("\n【更新後的書籍資料】")
    read_all_books(db)

    # 刪除書籍
    delete_books(db)

    # 顯示刪除後的資料
    print("\n【刪除後的書籍資料】")
    read_all_books(db)

    # 關閉資料庫
    db.close()
    print("\n✓ 資料庫已關閉")


if __name__ == "__main__":
    main()
