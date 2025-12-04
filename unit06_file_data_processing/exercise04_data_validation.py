"""exercise04_data_validation.py

練習 4：資料驗證與錯誤處理（難度：⭐⭐⭐）

任務：
1. 建立一個函式 validate_student_data(data)，驗證學生資料格式
2. 建立一個函式 safe_read_csv(filename)，安全地讀取 CSV 並處理錯誤
3. 建立一個函式 process_grades_with_validation(filename)，處理成績並驗證資料
4. 測試各種錯誤情況（檔案不存在、格式錯誤、資料無效等）
"""

import csv


def validate_student_data(data):
    """
    驗證學生資料格式

    規則：
    - name: 必須是非空字串
    - age: 必須是 15-30 之間的整數
    - score: 必須是 0-100 之間的數字
    """
    errors = []

    # 檢查姓名
    if "name" not in data or not data["name"].strip():
        errors.append("姓名為空或不存在")

    # 檢查年齡
    if "age" not in data:
        errors.append("年齡欄位不存在")
    else:
        try:
            age = int(data["age"])
            if age < 15 or age > 30:
                errors.append(f"年齡 {age} 不在有效範圍（15-30）")
        except ValueError:
            errors.append(f"年齡 '{data['age']}' 不是有效數字")

    # 檢查成績
    if "score" not in data:
        errors.append("成績欄位不存在")
    else:
        try:
            score = float(data["score"])
            if score < 0 or score > 100:
                errors.append(f"成績 {score} 不在有效範圍（0-100）")
        except ValueError:
            errors.append(f"成績 '{data['score']}' 不是有效數字")

    return errors


def safe_read_csv(filename):
    """安全地讀取 CSV 並處理錯誤"""
    print(f"=== 嘗試讀取：{filename} ===")

    try:
        with open(filename, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        print(f"✓ 成功讀取 {len(data)} 筆資料")
        return data

    except FileNotFoundError:
        print(f"✗ 錯誤：檔案 {filename} 不存在")
        return None

    except PermissionError:
        print(f"✗ 錯誤：沒有權限讀取檔案 {filename}")
        return None

    except csv.Error as e:
        print(f"✗ 錯誤：CSV 格式錯誤 - {e}")
        return None

    except Exception as e:
        print(f"✗ 未預期的錯誤：{e}")
        return None


def process_grades_with_validation(filename):
    """處理成績並驗證資料"""
    print(f"\n=== 處理並驗證成績資料 ===")

    # 安全讀取檔案
    data = safe_read_csv(filename)
    if data is None:
        return

    valid_count = 0
    invalid_count = 0
    valid_students = []

    # 逐筆驗證
    for row_num, row in enumerate(data, 2):  # 從第 2 行開始
        errors = validate_student_data(row)

        if errors:
            invalid_count += 1
            print(f"\n✗ 第 {row_num} 行資料無效：")
            for error in errors:
                print(f"    - {error}")
        else:
            valid_count += 1
            valid_students.append(row)
            print(f"✓ 第 {row_num} 行：{row['name']} - 資料有效")

    # 顯示統計
    print(f"\n--- 驗證結果 ---")
    print(f"總筆數：{len(data)}")
    print(f"有效：{valid_count}")
    print(f"無效：{invalid_count}")

    # 如果有有效資料，計算統計
    if valid_students:
        print(f"\n--- 有效資料統計 ---")
        scores = [float(s["score"]) for s in valid_students]
        ages = [int(s["age"]) for s in valid_students]

        print(
            f"成績：最高 {max(scores):.1f}，最低 {min(scores):.1f}，平均 {sum(scores)/len(scores):.2f}"
        )
        print(
            f"年齡：最大 {max(ages)}，最小 {min(ages)}，平均 {sum(ages)/len(ages):.1f}"
        )

    return valid_students


def create_test_files():
    """建立測試用的檔案"""
    print("=== 建立測試檔案 ===")

    # 正常檔案
    normal_data = [
        ["name", "age", "score"],
        ["小明", "20", "85"],
        ["小美", "19", "92"],
        ["阿強", "21", "78"],
    ]

    with open("normal_students.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(normal_data)
    print("✓ 已建立：normal_students.csv")

    # 包含錯誤的檔案
    error_data = [
        ["name", "age", "score"],
        ["小明", "20", "85"],  # 正常
        ["", "19", "92"],  # 姓名為空
        ["阿強", "abc", "78"],  # 年齡格式錯誤
        ["阿花", "21", "150"],  # 成績超過範圍
        ["小華", "10", "88"],  # 年齡太小
        ["小李", "22", "-10"],  # 成績為負
        ["小王", "25", "95"],  # 正常
    ]

    with open("error_students.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(error_data)
    print("✓ 已建立：error_students.csv")


if __name__ == "__main__":
    # 建立測試檔案
    create_test_files()

    # 測試正常檔案
    print("\n" + "=" * 50)
    process_grades_with_validation("normal_students.csv")

    # 測試包含錯誤的檔案
    print("\n" + "=" * 50)
    process_grades_with_validation("error_students.csv")

    # 測試不存在的檔案
    print("\n" + "=" * 50)
    process_grades_with_validation("不存在的檔案.csv")

    print("\n=== 完成 ===")
