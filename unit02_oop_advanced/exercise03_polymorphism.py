# 單元 2 練習 3：多型應用（難度：⭐⭐⭐）
# 學校要開辦「學生成果分享會」，不同科系的學生用不同方式展示自己的成果


class Student:
    def __init__(self, name):
        """
        初始化學生
        :param name: 學生姓名
        """
        self.name = name

    def demonstrate(self):
        """展示方法（基類別）"""
        print(f"{self.name} 進行演示")


class ComputerStudent(Student):
    def demonstrate(self):
        """資訊系學生展示 Python 程式"""
        print(f"{self.name}展示了一個 Python 程式")


class EnglishStudent(Student):
    def demonstrate(self):
        """英文系學生朗讀英文文章"""
        print(f"{self.name}朗讀了一篇英文文章")


def student_showcase(students_list):
    """
    多型應用：接收學生清單，對每個學生呼叫 demonstrate() 方法
    不用管具體是什麼類型的學生，只要都有 demonstrate() 方法就行

    :param students_list: 學生物件清單
    """
    for student in students_list:
        student.demonstrate()


if __name__ == "__main__":
    # 建立包含不同科系學生的清單
    students = [
        ComputerStudent("小明"),
        EnglishStudent("小花"),
        ComputerStudent("大衛"),
    ]

    # 進行學生成果分享（多型應用）
    student_showcase(students)
