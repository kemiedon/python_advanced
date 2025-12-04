"""example01_basic_file.py

示範基本檔案讀寫操作
"""

import os


def demo_write():
    """示範寫入檔案"""
    print("=== 示範寫入檔案 ===")

    # 寫入檔案（會覆蓋原有內容）
    with open("sample_data.txt", "w", encoding="utf-8") as f:
        f.write("第一行文字\n")
        f.write("第二行文字\n")
        f.write("第三行文字\n")

    print("✓ 檔案寫入完成：sample_data.txt")


def demo_read():
    """示範讀取檔案"""
    print("\n=== 示範讀取檔案 ===")

    # 一次讀取全部內容
    with open("sample_data.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("檔案內容：")
        print(content)


def demo_read_lines():
    """示範逐行讀取"""
    print("=== 示範逐行讀取 ===")

    with open("sample_data.txt", "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            print(f"第 {line_num} 行：{line.strip()}")


def demo_append():
    """示範附加內容"""
    print("\n=== 示範附加內容 ===")

    # 附加模式（不會覆蓋原有內容）
    with open("sample_data.txt", "a", encoding="utf-8") as f:
        f.write("第四行文字（附加）\n")

    print("✓ 內容已附加")

    # 再次讀取確認
    with open("sample_data.txt", "r", encoding="utf-8") as f:
        print("更新後的內容：")
        print(f.read())


def demo_check_exists():
    """示範檢查檔案是否存在"""
    print("=== 檢查檔案是否存在 ===")

    filename = "sample_data.txt"
    if os.path.exists(filename):
        print(f"✓ 檔案 {filename} 存在")
        print(f"  檔案大小：{os.path.getsize(filename)} bytes")
    else:
        print(f"✗ 檔案 {filename} 不存在")


if __name__ == "__main__":
    demo_write()
    demo_read()
    demo_read_lines()
    demo_append()
    demo_check_exists()

    print("\n=== 完成 ===")
