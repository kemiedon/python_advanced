"""exercise01_read_write.py

練習 1：讀寫文字檔案（難度：⭐）

任務：
1. 建立一個函式 create_diary(filename, content)，將日記內容寫入檔案
2. 建立一個函式 read_diary(filename)，讀取並顯示日記內容
3. 建立一個函式 append_diary(filename, content)，在日記後面追加新內容
4. 測試上述三個函式
"""


def create_diary(filename, content):
    """建立日記檔案並寫入內容"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ 日記已建立：{filename}")


def read_diary(filename):
    """讀取並顯示日記內容"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\n=== 日記內容 ===")
        print(content)
        return content
    except FileNotFoundError:
        print(f"✗ 找不到檔案：{filename}")
        return None


def append_diary(filename, content):
    """在日記後面追加新內容"""
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n" + content)
        print(f"✓ 內容已追加到：{filename}")
    except FileNotFoundError:
        print(f"✗ 找不到檔案：{filename}")


if __name__ == "__main__":
    # 測試建立日記
    create_diary("my_diary.txt", "2025-12-03\n今天天氣很好，學了很多 Python 知識。")

    # 測試讀取日記
    read_diary("my_diary.txt")

    # 測試追加內容
    append_diary("my_diary.txt", "晚上複習了檔案處理，覺得很有成就感！")

    # 再次讀取確認
    read_diary("my_diary.txt")

    print("\n=== 完成 ===")
