"""
練習 3：成績統計系統 ⭐⭐⭐

任務：
建立學生成績管理系統，包含多個資料表和統計功能。

要求：
1. 建立三個資料表：
   - students: 學生資料（學號、姓名、班級）
   - subjects: 科目資料（科目代碼、科目名稱）
   - scores: 成績資料（學號、科目代碼、成績）
2. 實作功能：
   - 新增學生、科目、成績
   - 查詢學生的所有成績
   - 計算學生的平均成績
   - 統計科目的平均分數
   - 找出每個科目的最高分學生
   - 列出不及格（< 60）的成績記錄

提示：
- 使用 JOIN 連接多個資料表
- 使用 GROUP BY 進行分組統計
- 使用子查詢找出最高分
"""

import sqlite3


class GradeManager:
    """成績管理系統"""

    def __init__(self, db_name="grades.db"):
        """
        初始化成績管理系統

        TODO: 實作初始化
        - 連接資料庫
        - 建立所需的資料表
        """
        pass

    def create_tables(self):
        """
        建立資料表

        TODO: 實作資料表建立
        - students 表
        - subjects 表
        - scores 表（外鍵關聯）
        """
        pass

    def add_student(self, student_id, name, class_name):
        """
        新增學生

        TODO: 實作新增學生
        """
        pass

    def add_subject(self, subject_code, subject_name):
        """
        新增科目

        TODO: 實作新增科目
        """
        pass

    def add_score(self, student_id, subject_code, score):
        """
        新增成績

        TODO: 實作新增成績
        - 檢查學生和科目是否存在
        - 檢查成績範圍（0-100）
        """
        pass

    def get_student_scores(self, student_id):
        """
        查詢學生的所有成績

        TODO: 實作成績查詢
        - 使用 JOIN 連接 scores 和 subjects
        - 顯示科目名稱和成績
        """
        pass

    def calculate_student_average(self, student_id):
        """
        計算學生的平均成績

        TODO: 實作平均成績計算
        - 使用 AVG() 函數
        """
        pass

    def calculate_subject_average(self, subject_code):
        """
        計算科目的平均分數

        TODO: 實作科目平均計算
        """
        pass

    def find_top_students_by_subject(self):
        """
        找出每個科目的最高分學生

        TODO: 實作最高分查詢
        - 使用 MAX() 和 GROUP BY
        - 顯示科目、學生和分數
        """
        pass

    def find_failing_scores(self):
        """
        列出不及格的成績記錄

        TODO: 實作不及格查詢
        - 分數 < 60
        - 顯示學生、科目和分數
        """
        pass

    def close(self):
        """關閉資料庫連接"""
        pass


def main():
    """主程式"""
    print("成績統計系統")
    print("=" * 60)

    # 建立管理系統
    manager = GradeManager()

    # 新增學生
    print("\n【新增學生】")
    manager.add_student("S001", "王小明", "一年A班")
    manager.add_student("S002", "李小華", "一年A班")
    manager.add_student("S003", "張大同", "一年B班")

    # 新增科目
    print("\n【新增科目】")
    manager.add_subject("MATH", "數學")
    manager.add_subject("ENG", "英文")
    manager.add_subject("PHY", "物理")

    # 新增成績
    print("\n【新增成績】")
    manager.add_score("S001", "MATH", 85)
    manager.add_score("S001", "ENG", 78)
    manager.add_score("S001", "PHY", 92)
    manager.add_score("S002", "MATH", 92)
    manager.add_score("S002", "ENG", 55)
    manager.add_score("S002", "PHY", 88)
    manager.add_score("S003", "MATH", 76)
    manager.add_score("S003", "ENG", 82)
    manager.add_score("S003", "PHY", 58)

    # 查詢學生成績
    print("\n【王小明的成績】")
    manager.get_student_scores("S001")

    # 計算平均
    print("\n【平均成績】")
    avg = manager.calculate_student_average("S001")
    print(f"王小明的平均成績: {avg:.2f}")

    # 科目平均
    print("\n【數學科平均】")
    avg = manager.calculate_subject_average("MATH")
    print(f"數學平均分數: {avg:.2f}")

    # 最高分
    print("\n【各科最高分】")
    manager.find_top_students_by_subject()

    # 不及格
    print("\n【不及格記錄】")
    manager.find_failing_scores()

    manager.close()


if __name__ == "__main__":
    main()
