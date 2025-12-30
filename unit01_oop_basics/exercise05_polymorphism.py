# 練習 5：多型應用（難度：⭐⭐⭐）
# 使用多型統一處理不同科系學生的選課行為
class Student:
    def __init__(self, name):
        """
        初始化學生
        :param name: 學生姓名
        """
        self.name = name
        self.courses = []  # 已修課程清單

    def enroll_course(self, course_name):
        """
        選課方法（基類別）
        :param course_name: 課程名稱
        """
        self.courses.append(course_name)
        print(f"{self.name} 選課 {course_name}：成功！")

    def get_courses(self):
        """查看已選課程"""
        return self.courses


class ComputerStudent(Student):
    """資訊系學生"""

    def enroll_course(self, course_name):
        """覆寫選課方法：只能選資訊相關課程"""
        keywords = ["資訊", "程式", "Python", "Java", "資料結構"]
        if any(keyword in course_name for keyword in keywords):
            super().enroll_course(course_name)
        else:
            print(f"{self.name} 選課 {course_name}：此課程不適合資訊系")


class EnglishStudent(Student):
    """英文系學生"""

    def enroll_course(self, course_name):
        """覆寫選課方法：只能選英文相關課程"""
        keywords = ["英文", "英語", "文學", "莎士比亞"]
        if any(keyword in course_name for keyword in keywords):
            super().enroll_course(course_name)
        else:
            print(f"{self.name} 選課 {course_name}：此課程不適合英文系")


def batch_enroll(students_list, course_name):
    """
    多型應用：統一為多個學生選課
    不需要判斷學生是什麼類型，直接呼叫 enroll_course() 方法
    每個學生會根據自己的規則決定是否能選課

    :param students_list: 學生物件清單
    :param course_name: 課程名稱
    """
    print(f"\n===== 開始選課：{course_name} =====")
    for student in students_list:
        student.enroll_course(course_name)


if __name__ == "__main__":
    # 建立不同科系的學生清單
    students = [
        ComputerStudent("小明"),
        EnglishStudent("小花"),
        ComputerStudent("大衛"),
        EnglishStudent("小美"),
    ]

    # 多型應用：統一為所有學生選課（各自根據規則判斷）
    batch_enroll(students, "Python")
    batch_enroll(students, "英文文學")
    batch_enroll(students, "資料結構")

    # 顯示所有學生的已選課程
    print("\n===== 選課結果 =====")
    for student in students:
        print(f"{student.name}：{student.get_courses()}")
