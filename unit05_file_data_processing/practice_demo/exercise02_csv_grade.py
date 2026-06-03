"""exercise02_csv_grade.py

練習 2：處理 CSV 成績資料（難度：⭐⭐）

任務：
1. 建立一個函式 create_grade_csv(filename)，產生包含學生成績的 CSV 檔案
2. 建立一個函式 calculate_averages(filename)，計算每位學生的平均分數
3. 建立一個函式 find_top_students(filename, n)，找出成績前 n 名的學生
4. 建立一個函式 export_with_rank(input_file, output_file)，輸出包含排名的新 CSV
"""

import csv


def create_grade_csv(filename):
    """產生包含學生成績的 CSV 檔案"""
    students = [
        ["學號", "姓名", "國文", "英文", "數學"],
        ["S001", "小明", "85", "90", "88"],
        ["S002", "小美", "92", "87", "95"],
        ["S003", "阿強", "78", "82", "80"],
        ["S004", "阿花", "88", "91", "86"],
        ["S005", "小華", "95", "89", "92"],
    ]

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(students)

    print(f"✓ 成績檔案已建立：{filename}")


def calculate_averages(filename):
    """計算每位學生的平均分數"""
    print(f"\n=== 計算平均分數 ===")

    averages = []

    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["姓名"]
            chinese = int(row["國文"])
            english = int(row["英文"])
            math = int(row["數學"])
            avg = (chinese + english + math) / 3

            averages.append({"姓名": name, "平均": avg})
            print(f"{name}：平均 {avg:.2f} 分")

    return averages


def find_top_students(filename, n):
    """找出成績前 n 名的學生"""
    print(f"\n=== 前 {n} 名學生 ===")

    students = []

    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["姓名"]
            chinese = int(row["國文"])
            english = int(row["英文"])
            math = int(row["數學"])
            avg = (chinese + english + math) / 3

            students.append({"學號": row["學號"], "姓名": name, "平均": avg})

    # 依平均分數排序（由高到低）
    students.sort(key=lambda x: x["平均"], reverse=True)

    # 取前 n 名
    top_students = students[:n]

    for rank, student in enumerate(top_students, 1):
        print(f"第 {rank} 名：{student['姓名']} （{student['平均']:.2f} 分）")

    return top_students


def export_with_rank(input_file, output_file):
    """輸出包含排名的新 CSV"""
    print(f"\n=== 輸出包含排名的檔案 ===")

    students = []

    # 讀取資料並計算平均
    with open(input_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            chinese = int(row["國文"])
            english = int(row["英文"])
            math = int(row["數學"])
            avg = (chinese + english + math) / 3

            students.append(
                {
                    "學號": row["學號"],
                    "姓名": row["姓名"],
                    "國文": row["國文"],
                    "英文": row["英文"],
                    "數學": row["數學"],
                    "平均": f"{avg:.2f}",
                }
            )

    # 依平均分數排序
    students.sort(key=lambda x: float(x["平均"]), reverse=True)

    # 加上排名
    for rank, student in enumerate(students, 1):
        student["排名"] = rank

    # 寫入新檔案
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["排名", "學號", "姓名", "國文", "英文", "數學", "平均"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

    print(f"✓ 已輸出到：{output_file}")


if __name__ == "__main__":
    # 建立測試檔案
    create_grade_csv("grades.csv")

    # 計算平均分數
    calculate_averages("grades.csv")

    # 找出前 3 名
    find_top_students("grades.csv", 3)

    # 輸出包含排名的檔案
    export_with_rank("grades.csv", "grades_with_rank.csv")

    print("\n=== 完成 ===")
