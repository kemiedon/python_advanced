"""
練習 1：JSON 筆記本 ⭐⭐

任務：
使用 JSON 建立一個簡單的筆記本系統。

要求：
1. 實作 NotesManager 類別
2. 支援新增、查詢、更新、刪除筆記
3. 每則筆記包含：標題、內容、標籤、建立時間、更新時間
4. 支援依標籤篩選筆記
5. 資料存入 notes.json 檔案

提示：
- 使用 datetime 模組記錄時間
- 標籤使用列表儲存，方便多標籤
- 實作搜尋時可使用字串包含比對
"""

import json
import os
from datetime import datetime


class NotesManager:
    """筆記管理系統"""

    def __init__(self, filename="notes.json"):
        """
        初始化筆記管理系統

        TODO: 實作初始化邏輯
        - 設定檔案名稱
        - 載入現有筆記
        """
        pass

    def load_notes(self):
        """
        載入筆記資料

        TODO: 實作載入邏輯
        - 如果檔案存在，讀取 JSON
        - 如果檔案不存在或格式錯誤，回傳空列表
        """
        pass

    def save_notes(self):
        """
        儲存筆記資料

        TODO: 實作儲存邏輯
        - 將筆記資料寫入 JSON 檔案
        - 設定適當的格式（縮排、中文支援）
        """
        pass

    def add_note(self, title, content, tags=None):
        """
        新增筆記

        TODO: 實作新增邏輯
        - 生成唯一 ID
        - 記錄建立時間
        - 處理標籤（如果沒有標籤，設為空列表）
        - 儲存筆記
        """
        pass

    def get_all_notes(self):
        """
        取得所有筆記

        TODO: 實作取得所有筆記的邏輯
        """
        pass

    def find_by_title(self, keyword):
        """
        依標題搜尋筆記

        TODO: 實作搜尋邏輯
        - 支援部分比對
        - 回傳符合的筆記列表
        """
        pass

    def find_by_tag(self, tag):
        """
        依標籤搜尋筆記

        TODO: 實作標籤搜尋邏輯
        - 找出包含指定標籤的所有筆記
        """
        pass

    def update_note(self, note_id, title=None, content=None, tags=None):
        """
        更新筆記

        TODO: 實作更新邏輯
        - 找到指定 ID 的筆記
        - 更新提供的欄位
        - 記錄更新時間
        """
        pass

    def delete_note(self, note_id):
        """
        刪除筆記

        TODO: 實作刪除邏輯
        - 找到並移除指定 ID 的筆記
        """
        pass


def test_notes_manager():
    """測試筆記管理系統"""
    print("測試 JSON 筆記本系統")
    print("=" * 60)

    # 建立管理器
    manager = NotesManager()

    # 測試新增
    print("\n【測試新增筆記】")
    manager.add_note("Python 學習筆記", "今天學了 JSON 操作", ["Python", "學習"])
    manager.add_note("待辦事項", "完成單元 8 練習", ["TODO"])
    manager.add_note("會議記錄", "下週一專案會議", ["工作", "會議"])

    # 測試查詢所有
    print("\n【所有筆記】")
    all_notes = manager.get_all_notes()
    for note in all_notes:
        print(f"ID {note['id']}: {note['title']}")
        print(f"  內容: {note['content']}")
        print(f"  標籤: {', '.join(note['tags'])}")
        print(f"  時間: {note['created_at']}")

    # 測試標題搜尋
    print("\n【搜尋「學習」】")
    results = manager.find_by_title("學習")
    for note in results:
        print(f"- {note['title']}")

    # 測試標籤搜尋
    print("\n【搜尋標籤「工作」】")
    results = manager.find_by_tag("工作")
    for note in results:
        print(f"- {note['title']}")

    # 測試更新
    print("\n【更新筆記】")
    manager.update_note(1, content="今天學了 JSON 和 TinyDB")

    # 測試刪除
    print("\n【刪除筆記】")
    manager.delete_note(2)

    print("\n【最終筆記】")
    all_notes = manager.get_all_notes()
    print(f"共有 {len(all_notes)} 則筆記")


if __name__ == "__main__":
    test_notes_manager()
