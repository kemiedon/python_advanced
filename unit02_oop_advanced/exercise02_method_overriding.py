# 單元 2 練習 2：子類別覆寫方法（難度：⭐⭐）
# 學校有不同科系的學生，他們除了基本資訊外，還需要顯示自己的專長


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


class ComputerStudent(Student):
    def __init__(self, name, student_id, programming_language):
        """
        初始化資訊系學生
        :param name: 學生姓名
        :param student_id: 學號
        :param programming_language: 主要程式語言
        """
        super().__init__(name, student_id)
        self.programming_language = programming_language

    def show_info(self):
        """覆寫父類別方法，顯示專長"""
        print(f"我是 {self.name}，專長是 {self.programming_language}")


class EnglishStudent(Student):
    def __init__(self, name, student_id, language_level):
        """
        初始化英文系學生
        :param name: 學生姓名
        :param student_id: 學號
        :param language_level: 英文程度
        """
        super().__init__(name, student_id)
        self.language_level = language_level

    def show_info(self):
        """覆寫父類別方法，顯示英文程度"""
        print(f"我是 {self.name}，英文程度是 {self.language_level}")


if __name__ == "__main__":
    # 建立不同科系的學生
    comp_student = ComputerStudent("小明", "S001", "Python")
    eng_student = EnglishStudent("小花", "S002", "Advanced")

    # 呼叫各自的 show_info() 方法
    comp_student.show_info()
    eng_student.show_info()
