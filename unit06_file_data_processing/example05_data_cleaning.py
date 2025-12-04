"""example05_data_cleaning.py

示範資料清理與轉換
"""

import csv


def demo_create_dirty_data():
    """建立包含髒資料的 CSV 檔案"""
    print("=== 建立測試用髒資料 ===")

    dirty_data = [
        ["姓名", "年齡", "成績", "備註"],
        ["小明", "20", "85", "正常"],
        ["小美", "", "92", "缺年齡"],
        ["阿強", "21", "", "缺成績"],
        ["阿花", "abc", "88", "年齡格式錯誤"],
        ["", "19", "95", "缺姓名"],
        ["小華", "22", "150", "成績超過範圍"],
        ["小李", "22", "78", "正常"],
    ]

    with open("dirty_students.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(dirty_data)

    print("✓ 已建立測試檔案：dirty_students.csv")


def demo_identify_problems():
    """識別資料中的問題"""
    print("\n=== 識別資料問題 ===")

    problems = []

    with open("dirty_students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, 2):  # 從第 2 行開始（第 1 行是標題）
            # 檢查姓名
            if not row["姓名"].strip():
                problems.append(f"第 {row_num} 行：姓名為空")

            # 檢查年齡
            try:
                age = int(row["年齡"])
                if age < 0 or age > 150:
                    problems.append(f"第 {row_num} 行：年齡 {age} 不合理")
            except ValueError:
                if row["年齡"].strip():
                    problems.append(f"第 {row_num} 行：年齡 '{row['年齡']}' 不是數字")
                else:
                    problems.append(f"第 {row_num} 行：年齡為空")

            # 檢查成績
            try:
                score = int(row["成績"])
                if score < 0 or score > 100:
                    problems.append(f"第 {row_num} 行：成績 {score} 超出範圍")
            except ValueError:
                if row["成績"].strip():
                    problems.append(f"第 {row_num} 行：成績 '{row['成績']}' 不是數字")
                else:
                    problems.append(f"第 {row_num} 行：成績為空")

    print(f"發現 {len(problems)} 個問題：")
    for problem in problems:
        print(f"  ✗ {problem}")


def demo_clean_data():
    """清理資料並產生乾淨的檔案"""
    print("\n=== 清理資料 ===")

    clean_rows = []
    skipped = 0
    fixed = 0

    with open("dirty_students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, 2):
            # 建立新的乾淨資料列
            clean_row = {}
            skip_row = False

            # 處理姓名
            name = row["姓名"].strip()
            if not name:
                print(f"  ✗ 跳過第 {row_num} 行：姓名為空")
                skipped += 1
                continue
            clean_row["姓名"] = name

            # 處理年齡
            try:
                age = int(row["年齡"])
                if age < 0 or age > 150:
                    print(f"  ⚠ 修正第 {row_num} 行：年齡 {age} → 20（預設值）")
                    age = 20
                    fixed += 1
            except ValueError:
                if row["年齡"].strip():
                    print(
                        f"  ⚠ 修正第 {row_num} 行：年齡 '{row['年齡']}' → 20（預設值）"
                    )
                else:
                    print(f"  ⚠ 修正第 {row_num} 行：年齡為空 → 20（預設值）")
                age = 20
                fixed += 1
            clean_row["年齡"] = age

            # 處理成績
            try:
                score = int(row["成績"])
                if score < 0:
                    score = 0
                    fixed += 1
                elif score > 100:
                    score = 100
                    fixed += 1
            except ValueError:
                if row["成績"].strip():
                    print(f"  ✗ 跳過第 {row_num} 行：成績 '{row['成績']}' 無效")
                else:
                    print(f"  ✗ 跳過第 {row_num} 行：成績為空")
                skipped += 1
                continue
            clean_row["成績"] = score

            clean_row["備註"] = row["備註"]
            clean_rows.append(clean_row)

    # 寫入乾淨的檔案
    with open("cleaned_students.csv", "w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["姓名", "年齡", "成績", "備註"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(clean_rows)

    print(f"\n✓ 清理完成：")
    print(f"  - 保留資料：{len(clean_rows)} 筆")
    print(f"  - 跳過資料：{skipped} 筆")
    print(f"  - 修正問題：{fixed} 項")
    print(f"  - 輸出檔案：cleaned_students.csv")


def demo_view_cleaned_data():
    """檢視清理後的資料"""
    print("\n=== 清理後的資料 ===")

    with open("cleaned_students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        print(f"{'姓名':<8} {'年齡':<6} {'成績':<6} {'備註'}")
        print("-" * 40)

        for row in reader:
            print(f"{row['姓名']:<8} {row['年齡']:<6} {row['成績']:<6} {row['備註']}")


def demo_statistics():
    """計算清理後資料的統計數據"""
    print("\n=== 資料統計 ===")

    scores = []
    ages = []

    with open("cleaned_students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            scores.append(int(row["成績"]))
            ages.append(int(row["年齡"]))

    if scores:
        print(f"成績統計：")
        print(f"  - 最高分：{max(scores)}")
        print(f"  - 最低分：{min(scores)}")
        print(f"  - 平均分：{sum(scores) / len(scores):.2f}")
        print(f"  - 總人數：{len(scores)}")

    if ages:
        print(f"\n年齡統計：")
        print(f"  - 最大年齡：{max(ages)}")
        print(f"  - 最小年齡：{min(ages)}")
        print(f"  - 平均年齡：{sum(ages) / len(ages):.2f}")


if __name__ == "__main__":
    demo_create_dirty_data()
    demo_identify_problems()
    demo_clean_data()
    demo_view_cleaned_data()
    demo_statistics()

    print("\n=== 完成 ===")
