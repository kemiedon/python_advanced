"""example02_csv_operations.py

示範 CSV 檔案處理
"""

import csv


def demo_write_csv():
    """示範寫入 CSV 檔案"""
    print("=== 示範寫入 CSV 檔案 ===")

    # 學生成績資料
    students_data = [
        ["姓名", "國文", "英文", "數學"],
        ["小明", "85", "90", "88"],
        ["小美", "92", "87", "95"],
        ["阿強", "78", "82", "80"],
        ["阿花", "88", "91", "86"],
    ]

    # 寫入 CSV
    with open("students.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(students_data)

    print("✓ CSV 檔案寫入完成：students.csv")


def demo_read_csv():
    """示範讀取 CSV 檔案"""
    print("\n=== 示範讀取 CSV 檔案 ===")

    with open("students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def demo_csv_with_dict():
    """示範使用字典方式處理 CSV"""
    print("\n=== 使用字典方式讀取 CSV ===")

    with open("students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(
                f"{row['姓名']}：國文 {row['國文']}，英文 {row['英文']}，數學 {row['數學']}"
            )


def demo_calculate_average():
    """示範計算平均分數"""
    print("\n=== 計算每位學生的平均分數 ===")

    with open("students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["姓名"]
            chinese = int(row["國文"])
            english = int(row["英文"])
            math = int(row["數學"])
            avg = (chinese + english + math) / 3

            print(f"{name}：平均 {avg:.2f} 分")


def demo_add_average_column():
    """示範新增平均分數欄位並寫入新檔案"""
    print("\n=== 新增平均分數欄位 ===")

    # 讀取原始資料並計算平均
    rows = []
    with open("students.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            chinese = int(row["國文"])
            english = int(row["英文"])
            math = int(row["數學"])
            avg = (chinese + english + math) / 3

            row["平均"] = f"{avg:.2f}"
            rows.append(row)

    # 寫入新檔案
    with open("students_with_avg.csv", "w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["姓名", "國文", "英文", "數學", "平均"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    print("✓ 已新增平均分數並寫入：students_with_avg.csv")


if __name__ == "__main__":
    demo_write_csv()
    demo_read_csv()
    demo_csv_with_dict()
    demo_calculate_average()
    demo_add_average_column()

    print("\n=== 完成 ===")
