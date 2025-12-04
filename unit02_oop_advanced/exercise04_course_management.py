# 單元 2 練習 4：綜合應用 - 課程管理系統（難度：⭐⭐⭐⭐）
# 設計一個簡單的課程管理系統，讓不同科系學生可以註冊課程


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
        print(f"{self.name}選課 {course_name}：成功！")

    def get_courses(self):
        """取得已選課程清單"""
        return self.courses


class ComputerStudent(Student):
    """資訊系學生"""

    ALLOWED_KEYWORDS = ["資訊", "程式", "Python", "Java", "資料結構"]

    def enroll_course(self, course_name):
        """
        覆寫父類別方法：只能選「資訊」相關課程
        :param course_name: 課程名稱
        """
        # 檢查課程是否適合資訊系
        if any(keyword in course_name for keyword in self.ALLOWED_KEYWORDS):
            super().enroll_course(course_name)
        else:
            print(f"{self.name}選課 {course_name}：此課程不適合資訊系")


class EnglishStudent(Student):
    """英文系學生"""

    ALLOWED_KEYWORDS = ["英文", "英語", "文學", "莎士比亞"]

    def enroll_course(self, course_name):
        """
        覆寫父類別方法：只能選「英文」相關課程
        :param course_name: 課程名稱
        """
        # 檢查課程是否適合英文系
        if any(keyword in course_name for keyword in self.ALLOWED_KEYWORDS):
            super().enroll_course(course_name)
        else:
            print(f"{self.name}選課 {course_name}：此課程不適合英文系")


if __name__ == "__main__":
    # 建立小明（資訊系）
    ming = ComputerStudent("小明")
    ming.enroll_course("Python")  # 成功
    ming.enroll_course("莎士比亞")  # 失敗
    print(f"小明已修課程：{ming.get_courses()}\n")

    # 建立小花（英文系）
    xiaohui = EnglishStudent("小花")
    xiaohui.enroll_course("英文文學")  # 成功
    xiaohui.enroll_course("資料結構")  # 失敗
    print(f"小花已修課程：{xiaohui.get_courses()}")
