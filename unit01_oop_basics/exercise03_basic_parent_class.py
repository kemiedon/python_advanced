# 練習 3：建立父類別 Student（難度：⭐⭐）
# 學校要建立課程管理系統，讓學生可以選課和查看已選課程

class Student:
    def __init__(self, name):
        """
        初始化學生
        :param name: 學生姓名
        """
        self.name = name
        self.courses = []  # 已修課程清單，初始為空

    def enroll_course(self, course_name):
        """
        選課方法
        :param course_name: 課程名稱
        """
        self.courses.append(course_name)
        print(f"{self.name} 選課 {course_name}：成功！")

    def get_courses(self):
        """
        查看已選課程
        :return: 已選課程清單
        """
        return self.courses


if __name__ == "__main__":
    # 建立學生實例
    student = Student("小明")

    # 選課
    student.enroll_course("Python")
    student.enroll_course("資料結構")

    # 查看已選課程
    print(f"\n{student.name} 已選課程：{student.get_courses()}")
