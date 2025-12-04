"""example04_error_handling.py

示範錯誤處理與資料驗證
"""

import os


def demo_file_not_found():
    """示範處理檔案不存在的錯誤"""
    print("=== 示範處理檔案不存在 ===")

    try:
        with open("不存在的檔案.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("✗ 錯誤：檔案不存在")
        print("→ 已處理錯誤，程式繼續執行")


def demo_value_error():
    """示範處理數值轉換錯誤"""
    print("\n=== 示範處理數值轉換錯誤 ===")

    data = ["85", "90", "abc", "88"]

    for item in data:
        try:
            score = int(item)
            print(f"✓ 成功轉換：{item} → {score}")
        except ValueError:
            print(f"✗ 無法轉換：{item} 不是有效的數字")


def demo_multiple_exceptions():
    """示範處理多種錯誤"""
    print("\n=== 示範處理多種錯誤 ===")

    def read_and_sum(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                total = 0
                for line in f:
                    number = int(line.strip())
                    total += number
                return total
        except FileNotFoundError:
            print(f"✗ 檔案 {filename} 不存在")
            return None
        except ValueError as e:
            print(f"✗ 資料格式錯誤：{e}")
            return None
        except Exception as e:
            print(f"✗ 未預期的錯誤：{e}")
            return None

    # 建立測試檔案
    with open("numbers.txt", "w", encoding="utf-8") as f:
        f.write("10\n20\n30\n")

    result = read_and_sum("numbers.txt")
    if result is not None:
        print(f"✓ 總和：{result}")

    # 測試不存在的檔案
    result = read_and_sum("不存在.txt")


def demo_finally():
    """示範 finally 的用法"""
    print("\n=== 示範 finally ===")

    def process_file(filename):
        print(f"開始處理：{filename}")
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"✓ 成功讀取 {len(content)} 個字元")
        except FileNotFoundError:
            print("✗ 檔案不存在")
        finally:
            print("→ 無論成功或失敗，都會執行 finally")

    # 建立測試檔案
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("測試內容")

    process_file("test.txt")
    print()
    process_file("不存在.txt")


def demo_custom_validation():
    """示範自訂資料驗證"""
    print("\n=== 示範自訂資料驗證 ===")

    def validate_score(score):
        """驗證分數是否有效"""
        if not isinstance(score, (int, float)):
            raise TypeError("分數必須是數字")
        if score < 0 or score > 100:
            raise ValueError("分數必須在 0-100 之間")
        return True

    test_scores = [85, 120, -10, "abc", 95.5]

    for score in test_scores:
        try:
            validate_score(score)
            print(f"✓ {score} 是有效分數")
        except TypeError as e:
            print(f"✗ {score}：{e}")
        except ValueError as e:
            print(f"✗ {score}：{e}")


def demo_safe_file_operations():
    """示範安全的檔案操作模式"""
    print("\n=== 示範安全的檔案操作 ===")

    def safe_write(filename, content):
        """安全地寫入檔案"""
        try:
            # 先檢查目錄是否存在
            directory = os.path.dirname(filename)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            # 寫入檔案
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"✓ 成功寫入：{filename}")
            return True
        except PermissionError:
            print(f"✗ 權限不足：無法寫入 {filename}")
            return False
        except Exception as e:
            print(f"✗ 寫入失敗：{e}")
            return False

    safe_write("output.txt", "測試內容")
    safe_write("data/output.txt", "測試內容（含子目錄）")


if __name__ == "__main__":
    demo_file_not_found()
    demo_value_error()
    demo_multiple_exceptions()
    demo_finally()
    demo_custom_validation()
    demo_safe_file_operations()

    print("\n=== 完成 ===")
