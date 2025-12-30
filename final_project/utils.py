"""
工具函式模組
提供 JSON 備份、CSV 匯出等功能
"""

import json
import csv
from datetime import datetime
import os


def backup_to_json(data, filename=None):
    """將資料備份為 JSON 檔案"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"backup_{timestamp}.json"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ 備份成功：{filename}")
        return True
    except Exception as e:
        print(f"✗ 備份失敗：{e}")
        return False


def restore_from_json(filename):
    """從 JSON 檔案還原資料"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✓ 讀取備份成功：{filename}")
        return data
    except FileNotFoundError:
        print(f"✗ 檔案不存在：{filename}")
        return None
    except Exception as e:
        print(f"✗ 讀取備份失敗：{e}")
        return None


def export_to_csv(data, filename, headers=None):
    """將資料匯出為 CSV 檔案"""
    if not data:
        print("✗ 沒有資料可匯出")
        return False

    try:
        with open(filename, "w", encoding="utf-8-sig", newline="") as f:
            if headers is None:
                headers = data[0].keys()

            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"✓ CSV 匯出成功：{filename}")
        return True
    except Exception as e:
        print(f"✗ CSV 匯出失敗：{e}")
        return False


def export_grades_to_csv(grades_data, subject_name, filename=None):
    """匯出成績排名到 CSV"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_subject_name = subject_name.replace(" ", "_")
        filename = f"grades_{safe_subject_name}_{timestamp}.csv"

    headers = ["排名", "學號", "學生姓名", "分數"]
    csv_data = []

    for item in grades_data:
        csv_data.append(
            {
                "排名": item["rank"],
                "學號": item["student_id"],
                "學生姓名": item["student_name"],
                "分數": item["score"],
            }
        )

    return export_to_csv(csv_data, filename, headers)


def print_table(data, headers):
    """以表格形式顯示資料"""
    if not data:
        print("(無資料)")
        return

    # 計算每欄的最大寬度
    col_widths = {}
    for header in headers:
        col_widths[header] = len(str(header))

    for row in data:
        for header in headers:
            value = str(row.get(header, ""))
            col_widths[header] = max(col_widths[header], len(value))

    # 印出表頭
    header_line = " | ".join(str(h).ljust(col_widths[h]) for h in headers)
    print(header_line)
    print("-" * len(header_line))

    # 印出資料
    for row in data:
        row_line = " | ".join(str(row.get(h, "")).ljust(col_widths[h]) for h in headers)
        print(row_line)


def validate_email(email):
    """簡單的 Email 驗證"""
    return "@" in email and "." in email.split("@")[1]


def validate_score(score):
    """驗證分數範圍"""
    try:
        score = float(score)
        return 0 <= score <= 100
    except:
        return False


def get_user_input(prompt, input_type=str, validator=None):
    """取得使用者輸入並驗證"""
    while True:
        try:
            user_input = input(prompt)
            if user_input.strip() == "":
                print("✗ 輸入不可為空！")
                continue

            # 類型轉換
            value = input_type(user_input)

            # 自訂驗證
            if validator and not validator(value):
                print("✗ 輸入格式不正確！")
                continue

            return value
        except ValueError:
            print(f"✗ 請輸入有效的 {input_type.__name__} 類型！")
        except KeyboardInterrupt:
            print("\n操作已取消")
            return None


def clear_screen():
    """清除螢幕"""
    os.system("clear" if os.name != "nt" else "cls")


def print_separator(char="=", length=60):
    """印出分隔線"""
    print(char * length)


def print_title(title):
    """印出標題"""
    print_separator()
    print(f"  {title}")
    print_separator()
