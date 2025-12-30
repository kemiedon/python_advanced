# 練習 4：子類別覆寫方法（難度：⭐⭐⭐）
# 不同科系的學生有選課限制，需要覆寫 enroll_course() 方法

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
        """
        覆寫父類別方法：只能選「資訊」相關課程
        :param course_name: 課程名稱
        """
        # 定義資訊系相關關鍵字
        keywords = ["資訊", "程式", "Python", "Java", "資料結構"]

        # 檢查課程是否適合資訊系
        if any(keyword in course_name for keyword in keywords):
            super().enroll_course(course_name)
        else:
            print(f"{self.name} 選課 {course_name}：此課程不適合資訊系")


class EnglishStudent(Student):
    """英文系學生"""

    def enroll_course(self, course_name):
        """
        覆寫父類別方法：只能選「英文」相關課程
        :param course_name: 課程名稱
        """
        # 定義英文系相關關鍵字
        keywords = ["英文", "英語", "文學", "莎士比亞"]

        # 檢查課程是否適合英文系
        if any(keyword in course_name for keyword in keywords):
            super().enroll_course(course_name)
        else:
            print(f"{self.name} 選課 {course_name}：此課程不適合英文系")


if __name__ == "__main__":
    # 建立小明（資訊系）
    ming = ComputerStudent("小明")
    ming.enroll_course("Python")  # 成功
    ming.enroll_course("莎士比亞")  # 失敗
    print(f"小明已選課程：{ming.get_courses()}\n")

    # 建立小花（英文系）
    hua = EnglishStudent("小花")
    hua.enroll_course("英文文學")  # 成功
    hua.enroll_course("資料結構")  # 失敗
    print(f"小花已選課程：{hua.get_courses()}")
