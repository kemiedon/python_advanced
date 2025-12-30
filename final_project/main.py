"""
主程式入口
學生成績管理系統
"""

import sys
from database import Database
from utils import (
    backup_to_json,
    restore_from_json,
    export_grades_to_csv,
    print_table,
    validate_email,
    validate_score,
    get_user_input,
    clear_screen,
    print_separator,
    print_title,
)


class StudentManagementSystem:
    """學生管理系統主類別"""

    def __init__(self):
        self.db = Database()

    def run(self):
        """執行主程式"""
        while True:
            self.show_main_menu()
            choice = input("請選擇功能 (輸入數字): ").strip()

            if choice == "1":
                self.student_menu()
            elif choice == "2":
                self.subject_menu()
            elif choice == "3":
                self.grade_menu()
            elif choice == "4":
                self.report_menu()
            elif choice == "5":
                self.backup_menu()
            elif choice == "0":
                print("\n感謝使用！再見！")
                sys.exit(0)
            else:
                print("✗ 無效的選項，請重新輸入")

            input("\n按 Enter 繼續...")

    def show_main_menu(self):
        """顯示主選單"""
        clear_screen()
        print_title("學生成績管理系統")
        print("1. 學生管理")
        print("2. 科目管理")
        print("3. 成績管理")
        print("4. 報表查詢")
        print("5. 備份與匯出")
        print("0. 離開系統")
        print_separator()

    # ==================== 學生管理 ====================

    def student_menu(self):
        """學生管理選單"""
        while True:
            clear_screen()
            print_title("學生管理")
            print("1. 查看所有學生")
            print("2. 新增學生")
            print("3. 更新學生資料")
            print("4. 刪除學生")
            print("0. 返回主選單")
            print_separator()

            choice = input("請選擇功能: ").strip()

            if choice == "1":
                self.list_all_students()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "0":
                break
            else:
                print("✗ 無效的選項")

            if choice != "0":
                input("\n按 Enter 繼續...")

    def list_all_students(self):
        """列出所有學生"""
        print_title("所有學生列表")
        students = self.db.get_all_students()

        if not students:
            print("目前沒有學生資料")
            return

        data = [s.to_dict() for s in students]
        headers = ["student_id", "name", "age", "email"]
        print_table(data, headers)

    def add_student(self):
        """新增學生"""
        print_title("新增學生")

        name = get_user_input("請輸入學生姓名: ", str)
        if name is None:
            return

        age = get_user_input("請輸入年齡: ", int)
        if age is None:
            return

        email = get_user_input("請輸入 Email: ", str, validate_email)
        if email is None:
            return

        student_id = self.db.create_student(name, age, email)
        if student_id:
            print(f"✓ 新增成功！學生 ID: {student_id}")
        else:
            print("✗ 新增失敗")

    def update_student(self):
        """更新學生資料"""
        print_title("更新學生資料")
        self.list_all_students()

        student_id = get_user_input("\n請輸入要更新的學生 ID: ", int)
        if student_id is None:
            return

        student = self.db.get_student_by_id(student_id)
        if not student:
            print(f"✗ 找不到學生 ID: {student_id}")
            return

        print(f"\n目前資料：{student}")
        print("(若不修改某欄位，直接按 Enter)")

        name = input(f"新姓名 [{student.name}]: ").strip() or None

        age_input = input(f"新年齡 [{student.age}]: ").strip()
        age = int(age_input) if age_input else None

        email = input(f"新 Email [{student.email}]: ").strip() or None

        if self.db.update_student(student_id, name, age, email):
            print("✓ 更新成功")
        else:
            print("✗ 更新失敗")

    def delete_student(self):
        """刪除學生"""
        print_title("刪除學生")
        self.list_all_students()

        student_id = get_user_input("\n請輸入要刪除的學生 ID: ", int)
        if student_id is None:
            return

        confirm = input(f"確定要刪除學生 ID {student_id} 嗎？(y/n): ").strip().lower()
        if confirm == "y":
            if self.db.delete_student(student_id):
                print("✓ 刪除成功")
            else:
                print("✗ 刪除失敗")
        else:
            print("已取消刪除")

    # ==================== 科目管理 ====================

    def subject_menu(self):
        """科目管理選單"""
        while True:
            clear_screen()
            print_title("科目管理")
            print("1. 查看所有科目")
            print("2. 新增科目")
            print("3. 更新科目資料")
            print("4. 刪除科目")
            print("0. 返回主選單")
            print_separator()

            choice = input("請選擇功能: ").strip()

            if choice == "1":
                self.list_all_subjects()
            elif choice == "2":
                self.add_subject()
            elif choice == "3":
                self.update_subject()
            elif choice == "4":
                self.delete_subject()
            elif choice == "0":
                break
            else:
                print("✗ 無效的選項")

            if choice != "0":
                input("\n按 Enter 繼續...")

    def list_all_subjects(self):
        """列出所有科目"""
        print_title("所有科目列表")
        subjects = self.db.get_all_subjects()

        if not subjects:
            print("目前沒有科目資料")
            return

        data = [s.to_dict() for s in subjects]
        headers = ["subject_id", "subject_name", "credits"]
        print_table(data, headers)

    def add_subject(self):
        """新增科目"""
        print_title("新增科目")

        subject_name = get_user_input("請輸入科目名稱: ", str)
        if subject_name is None:
            return

        credits = get_user_input("請輸入學分數: ", int)
        if credits is None:
            return

        subject_id = self.db.create_subject(subject_name, credits)
        if subject_id:
            print(f"✓ 新增成功！科目 ID: {subject_id}")
        else:
            print("✗ 新增失敗（可能科目名稱已存在）")

    def update_subject(self):
        """更新科目資料"""
        print_title("更新科目資料")
        self.list_all_subjects()

        subject_id = get_user_input("\n請輸入要更新的科目 ID: ", int)
        if subject_id is None:
            return

        subject = self.db.get_subject_by_id(subject_id)
        if not subject:
            print(f"✗ 找不到科目 ID: {subject_id}")
            return

        print(f"\n目前資料：{subject}")
        print("(若不修改某欄位，直接按 Enter)")

        subject_name = input(f"新科目名稱 [{subject.subject_name}]: ").strip() or None

        credits_input = input(f"新學分數 [{subject.credits}]: ").strip()
        credits = int(credits_input) if credits_input else None

        if self.db.update_subject(subject_id, subject_name, credits):
            print("✓ 更新成功")
        else:
            print("✗ 更新失敗")

    def delete_subject(self):
        """刪除科目"""
        print_title("刪除科目")
        self.list_all_subjects()

        subject_id = get_user_input("\n請輸入要刪除的科目 ID: ", int)
        if subject_id is None:
            return

        confirm = input(f"確定要刪除科目 ID {subject_id} 嗎？(y/n): ").strip().lower()
        if confirm == "y":
            if self.db.delete_subject(subject_id):
                print("✓ 刪除成功")
            else:
                print("✗ 刪除失敗")
        else:
            print("已取消刪除")

    # ==================== 成績管理 ====================

    def grade_menu(self):
        """成績管理選單"""
        while True:
            clear_screen()
            print_title("成績管理")
            print("1. 新增/更新成績")
            print("2. 查詢學生成績")
            print("0. 返回主選單")
            print_separator()

            choice = input("請選擇功能: ").strip()

            if choice == "1":
                self.add_or_update_grade()
            elif choice == "2":
                self.view_student_grades()
            elif choice == "0":
                break
            else:
                print("✗ 無效的選項")

            if choice != "0":
                input("\n按 Enter 繼續...")

    def add_or_update_grade(self):
        """新增或更新成績"""
        print_title("新增/更新成績")

        print("=== 學生列表 ===")
        self.list_all_students()

        print("\n=== 科目列表 ===")
        self.list_all_subjects()

        student_id = get_user_input("\n請輸入學生 ID: ", int)
        if student_id is None:
            return

        # 驗證學生是否存在
        if not self.db.get_student_by_id(student_id):
            print("✗ 學生不存在")
            return

        subject_id = get_user_input("請輸入科目 ID: ", int)
        if subject_id is None:
            return

        # 驗證科目是否存在
        if not self.db.get_subject_by_id(subject_id):
            print("✗ 科目不存在")
            return

        score = get_user_input("請輸入分數 (0-100): ", float, validate_score)
        if score is None:
            return

        if self.db.add_grade(student_id, subject_id, score):
            print("✓ 成績登錄成功")
        else:
            print("✗ 成績登錄失敗")

    def view_student_grades(self):
        """查詢學生成績"""
        print_title("查詢學生成績")
        self.list_all_students()

        student_id = get_user_input("\n請輸入學生 ID: ", int)
        if student_id is None:
            return

        student = self.db.get_student_by_id(student_id)
        if not student:
            print("✗ 學生不存在")
            return

        grades = self.db.get_student_grades(student_id)

        print(f"\n{student.name} 的成績：")
        if not grades:
            print("(尚無成績記錄)")
            return

        headers = ["subject_name", "score", "credits"]
        print_table(grades, headers)

    # ==================== 報表查詢 ====================

    def report_menu(self):
        """報表查詢選單"""
        while True:
            clear_screen()
            print_title("報表查詢")
            print("1. 科目成績排名")
            print("2. 匯出科目成績 (CSV)")
            print("0. 返回主選單")
            print_separator()

            choice = input("請選擇功能: ").strip()

            if choice == "1":
                self.view_subject_ranking()
            elif choice == "2":
                self.export_subject_grades()
            elif choice == "0":
                break
            else:
                print("✗ 無效的選項")

            if choice != "0":
                input("\n按 Enter 繼續...")

    def view_subject_ranking(self):
        """查看科目成績排名"""
        print_title("科目成績排名")
        self.list_all_subjects()

        subject_id = get_user_input("\n請輸入科目 ID: ", int)
        if subject_id is None:
            return

        subject = self.db.get_subject_by_id(subject_id)
        if not subject:
            print("✗ 科目不存在")
            return

        grades = self.db.get_grades_by_subject(subject_id)

        print(f"\n【{subject.subject_name}】成績排名：")
        if not grades:
            print("(尚無成績記錄)")
            return

        headers = ["rank", "student_id", "student_name", "score"]
        print_table(grades, headers)

    def export_subject_grades(self):
        """匯出科目成績"""
        print_title("匯出科目成績 (CSV)")
        self.list_all_subjects()

        subject_id = get_user_input("\n請輸入科目 ID: ", int)
        if subject_id is None:
            return

        subject = self.db.get_subject_by_id(subject_id)
        if not subject:
            print("✗ 科目不存在")
            return

        grades = self.db.get_grades_by_subject(subject_id)

        if not grades:
            print("✗ 該科目尚無成績記錄")
            return

        export_grades_to_csv(grades, subject.subject_name)

    # ==================== 備份與匯出 ====================

    def backup_menu(self):
        """備份與匯出選單"""
        while True:
            clear_screen()
            print_title("備份與匯出")
            print("1. 備份所有資料 (JSON)")
            print("2. 從備份還原 (JSON)")
            print("0. 返回主選單")
            print_separator()

            choice = input("請選擇功能: ").strip()

            if choice == "1":
                self.backup_all_data()
            elif choice == "2":
                self.restore_data()
            elif choice == "0":
                break
            else:
                print("✗ 無效的選項")

            if choice != "0":
                input("\n按 Enter 繼續...")

    def backup_all_data(self):
        """備份所有資料"""
        print_title("備份所有資料")

        data = self.db.get_all_data()
        backup_to_json(data)

    def restore_data(self):
        """從備份還原"""
        print_title("從備份還原")

        filename = input("請輸入備份檔案名稱: ").strip()
        if not filename:
            print("✗ 檔案名稱不可為空")
            return

        data = restore_from_json(filename)
        if data:
            print("\n警告：還原資料將清除現有資料！")
            confirm = input("確定要繼續嗎？(y/n): ").strip().lower()
            if confirm != "y":
                print("已取消還原")
                return

            # 這裡可以實作還原邏輯
            # 需要先清除現有資料，再插入備份資料
            print("(還原功能需進一步實作)")


def main():
    """主函式"""
    try:
        system = StudentManagementSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n\n程式已中斷！")
        sys.exit(0)


if __name__ == "__main__":
    main()
