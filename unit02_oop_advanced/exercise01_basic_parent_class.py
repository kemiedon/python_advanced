# 單元 2 練習 1：基礎父類別設計（難度：⭐）
# 學校要管理學生資料，所有學生都有「姓名」和「學號」兩項基本資訊


class Student:
    def __init__(self, name, student_id):
        """
        初始化學生的基本資訊
        :param name: 學生姓名
        :param student_id: 學號
        """
        self.name = name
        self.student_id = student_id

    def show_info(self):
        """顯示學生的基本資訊"""
        print(f"我是 {self.name}，學號是 {self.student_id}")


if __name__ == "__main__":
    # 建立兩個學生實例
    student1 = Student("小明", "S001")
    student2 = Student("小花", "S002")

    # 呼叫 show_info() 方法
    student1.show_info()
    student2.show_info()
