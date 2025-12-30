"""
練習 2：TinyDB 待辦事項 ⭐⭐⭐

任務：
使用 TinyDB 建立待辦事項管理系統。

要求：
1. 實作 TodoManager 類別
2. 每個待辦事項包含：
   - 標題、描述、優先順序（高/中/低）
   - 狀態（待辦/進行中/已完成）
   - 建立時間、完成時間
3. 實作功能：
   - 新增待辦事項
   - 查詢待辦事項（依狀態、優先順序）
   - 更新狀態
   - 標記為完成
   - 刪除待辦事項
4. 使用 TinyDB 的查詢功能

提示：
- 使用 Query 物件進行查詢
- 優先順序可用數字表示（1=高、2=中、3=低）
- 完成時記錄完成時間
"""

from tinydb import TinyDB, Query
from datetime import datetime


class TodoManager:
    """待辦事項管理系統"""

    def __init__(self, db_name="todo.json"):
        """
        初始化待辦事項管理系統

        TODO: 實作初始化
        - 建立 TinyDB 資料庫
        """
        pass

    def add_todo(self, title, description="", priority="中"):
        """
        新增待辦事項

        TODO: 實作新增邏輯
        - 優先順序: 高/中/低
        - 初始狀態: 待辦
        - 記錄建立時間
        """
        pass

    def get_all_todos(self):
        """
        取得所有待辦事項

        TODO: 實作取得所有待辦事項
        """
        pass

    def get_by_status(self, status):
        """
        依狀態查詢

        TODO: 實作狀態查詢
        - 狀態: 待辦/進行中/已完成
        """
        pass

    def get_by_priority(self, priority):
        """
        依優先順序查詢

        TODO: 實作優先順序查詢
        """
        pass

    def update_status(self, doc_id, status):
        """
        更新狀態

        TODO: 實作狀態更新
        - 如果狀態改為「已完成」，記錄完成時間
        """
        pass

    def mark_completed(self, doc_id):
        """
        標記為完成

        TODO: 實作完成標記
        - 更新狀態為「已完成」
        - 記錄完成時間
        """
        pass

    def delete_todo(self, doc_id):
        """
        刪除待辦事項

        TODO: 實作刪除邏輯
        """
        pass

    def display_todos(self, todos):
        """顯示待辦事項"""
        if not todos:
            print("目前沒有待辦事項")
            return

        for todo in todos:
            print(f"\n{'='*60}")
            print(f"ID: {todo.doc_id}")
            print(f"標題: {todo['title']}")
            print(f"描述: {todo.get('description', '(無)')}")
            print(f"優先順序: {todo['priority']}")
            print(f"狀態: {todo['status']}")
            print(f"建立時間: {todo['created_at']}")
            if todo.get("completed_at"):
                print(f"完成時間: {todo['completed_at']}")

    def close(self):
        """關閉資料庫"""
        pass


def main():
    """主程式"""
    print("TinyDB 待辦事項管理")
    print("=" * 60)

    # 建立管理器
    manager = TodoManager()

    # 測試新增
    print("\n【新增待辦事項】")
    manager.add_todo("完成 Python 作業", "單元 8 練習", "高")
    manager.add_todo("買菜", "晚餐食材", "中")
    manager.add_todo("運動", "跑步 30 分鐘", "中")
    manager.add_todo("看書", "閱讀技術書籍", "低")

    # 顯示所有
    print("\n【所有待辦事項】")
    todos = manager.get_all_todos()
    manager.display_todos(todos)

    # 依狀態查詢
    print("\n【狀態為「待辦」的事項】")
    todos = manager.get_by_status("待辦")
    manager.display_todos(todos)

    # 依優先順序查詢
    print("\n【高優先順序的事項】")
    todos = manager.get_by_priority("高")
    manager.display_todos(todos)

    # 更新狀態
    print("\n【更新狀態】")
    manager.update_status(1, "進行中")

    # 標記完成
    print("\n【標記完成】")
    manager.mark_completed(2)

    # 顯示更新後的資料
    print("\n【更新後的待辦事項】")
    todos = manager.get_all_todos()
    manager.display_todos(todos)

    manager.close()


if __name__ == "__main__":
    main()
