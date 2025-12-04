"""exercise05_integrated_system.py

練習 5：綜合應用 - 學生成績管理系統（難度：⭐⭐⭐⭐）

任務：
整合前面學過的所有技術，建立一個完整的學生成績管理系統

功能需求：
1. 從 CSV 檔案載入學生資料
2. 新增、修改、刪除學生資料
3. 計算統計資料（平均、最高、最低）
4. 搜尋與篩選學生
5. 資料驗證與錯誤處理
6. 自動備份到 JSON
7. 匯出成績報表到 CSV
"""

import csv
import json
from datetime import datetime


class StudentGradeSystem:
    """學生成績管理系統"""

    def __init__(self):
        self.students = []
        self.modified = False

    def load_from_csv(self, filename):
        """從 CSV 檔案載入學生資料"""
        print(f"=== 載入資料：{filename} ===")

        try:
            with open(filename, "r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                self.students = []

                for row in reader:
                    student = {
                        "id": row["學號"],
                        "name": row["姓名"],
                        "chinese": int(row["國文"]),
                        "english": int(row["英文"]),
                        "math": int(row["數學"]),
                    }
                    self.students.append(student)

            print(f"✓ 成功載入 {len(self.students)} 筆學生資料")
            self.modified = False
            return True

        except FileNotFoundError:
            print(f"✗ 找不到檔案：{filename}")
            return False
        except Exception as e:
            print(f"✗ 載入失敗：{e}")
            return False

    def add_student(self, student_id, name, chinese, english, math):
        """新增學生"""
        # 驗證資料
        if not name.strip():
            print("✗ 姓名不能為空")
            return False

        if not (0 <= chinese <= 100 and 0 <= english <= 100 and 0 <= math <= 100):
            print("✗ 成績必須在 0-100 之間")
            return False

        # 檢查學號是否重複
        for student in self.students:
            if student["id"] == student_id:
                print(f"✗ 學號 {student_id} 已存在")
                return False

        # 新增學生
        student = {
            "id": student_id,
            "name": name,
            "chinese": chinese,
            "english": english,
            "math": math,
        }

        self.students.append(student)
        self.modified = True
        print(f"✓ 已新增學生：{name} ({student_id})")
        return True

    def update_student(self, student_id, **kwargs):
        """更新學生資料"""
        for student in self.students:
            if student["id"] == student_id:
                if "name" in kwargs:
                    student["name"] = kwargs["name"]
                if "chinese" in kwargs:
                    student["chinese"] = kwargs["chinese"]
                if "english" in kwargs:
                    student["english"] = kwargs["english"]
                if "math" in kwargs:
                    student["math"] = kwargs["math"]

                self.modified = True
                print(f"✓ 已更新學生：{student['name']} ({student_id})")
                return True

        print(f"✗ 找不到學號：{student_id}")
        return False

    def delete_student(self, student_id):
        """刪除學生"""
        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                name = student["name"]
                del self.students[i]
                self.modified = True
                print(f"✓ 已刪除學生：{name} ({student_id})")
                return True

        print(f"✗ 找不到學號：{student_id}")
        return False

    def search_by_name(self, name):
        """依姓名搜尋學生"""
        results = [s for s in self.students if name in s["name"]]
        return results

    def calculate_average(self, student):
        """計算學生平均分數"""
        return (student["chinese"] + student["english"] + student["math"]) / 3

    def get_statistics(self):
        """取得統計資料"""
        if not self.students:
            return None

        averages = [self.calculate_average(s) for s in self.students]

        return {
            "total_students": len(self.students),
            "avg_score": sum(averages) / len(averages),
            "highest_score": max(averages),
            "lowest_score": min(averages),
            "highest_student": max(
                self.students, key=lambda s: self.calculate_average(s)
            )["name"],
            "lowest_student": min(
                self.students, key=lambda s: self.calculate_average(s)
            )["name"],
        }

    def display_all(self):
        """顯示所有學生"""
        print(f"\n=== 所有學生資料 ===")
        print(
            f"{'學號':<8} {'姓名':<8} {'國文':<6} {'英文':<6} {'數學':<6} {'平均':<8}"
        )
        print("-" * 55)

        for student in self.students:
            avg = self.calculate_average(student)
            print(
                f"{student['id']:<8} {student['name']:<8} "
                f"{student['chinese']:<6} {student['english']:<6} "
                f"{student['math']:<6} {avg:<8.2f}"
            )

    def display_statistics(self):
        """顯示統計資料"""
        stats = self.get_statistics()

        if stats is None:
            print("目前沒有學生資料")
            return

        print(f"\n=== 統計資料 ===")
        print(f"總學生數：{stats['total_students']}")
        print(f"平均分數：{stats['avg_score']:.2f}")
        print(f"最高分數：{stats['highest_score']:.2f} （{stats['highest_student']}）")
        print(f"最低分數：{stats['lowest_score']:.2f} （{stats['lowest_student']}）")

    def backup_to_json(self, filename=None):
        """備份到 JSON"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"backup_{timestamp}.json"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.students, f, ensure_ascii=False, indent=2)

            print(f"✓ 已備份到：{filename}")
            return True
        except Exception as e:
            print(f"✗ 備份失敗：{e}")
            return False

    def export_to_csv(self, filename):
        """匯出到 CSV"""
        try:
            with open(filename, "w", newline="", encoding="utf-8-sig") as f:
                fieldnames = ["學號", "姓名", "國文", "英文", "數學", "平均"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()

                for student in self.students:
                    avg = self.calculate_average(student)
                    writer.writerow(
                        {
                            "學號": student["id"],
                            "姓名": student["name"],
                            "國文": student["chinese"],
                            "英文": student["english"],
                            "數學": student["math"],
                            "平均": f"{avg:.2f}",
                        }
                    )

            print(f"✓ 已匯出到：{filename}")
            return True
        except Exception as e:
            print(f"✗ 匯出失敗：{e}")
            return False


def create_sample_data():
    """建立範例資料"""
    data = [
        ["學號", "姓名", "國文", "英文", "數學"],
        ["S001", "小明", "85", "90", "88"],
        ["S002", "小美", "92", "87", "95"],
        ["S003", "阿強", "78", "82", "80"],
        ["S004", "阿花", "88", "91", "86"],
    ]

    with open("sample_grades.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("✓ 已建立範例資料：sample_grades.csv")


if __name__ == "__main__":
    # 建立範例資料
    create_sample_data()

    # 建立系統實例
    system = StudentGradeSystem()

    # 載入資料
    system.load_from_csv("sample_grades.csv")

    # 顯示所有學生
    system.display_all()

    # 顯示統計
    system.display_statistics()

    # 新增學生
    print("\n--- 新增學生 ---")
    system.add_student("S005", "小華", 95, 89, 92)

    # 更新學生
    print("\n--- 更新學生 ---")
    system.update_student("S001", chinese=90, english=95)

    # 搜尋學生
    print("\n--- 搜尋學生（包含「小」）---")
    results = system.search_by_name("小")
    for student in results:
        avg = system.calculate_average(student)
        print(f"  {student['name']} ({student['id']})：平均 {avg:.2f}")

    # 刪除學生
    print("\n--- 刪除學生 ---")
    system.delete_student("S003")

    # 再次顯示所有學生
    system.display_all()

    # 再次顯示統計
    system.display_statistics()

    # 備份到 JSON
    print("\n--- 備份資料 ---")
    system.backup_to_json("students_backup.json")

    # 匯出到 CSV
    print("\n--- 匯出報表 ---")
    system.export_to_csv("grade_report.csv")

    print("\n=== 完成 ===")
