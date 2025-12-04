# 單元 1 練習 1：基礎類別設計（難度：⭐）
# 建立一個 Student 類別來管理學生的成績資料


class Student:
    def __init__(self, chinese, english, math):
        """
        初始化學生的三科成績
        :param chinese: 國文成績
        :param english: 英文成績
        :param math: 數學成績
        """
        self.chinese = chinese
        self.english = english
        self.math = math

    def average(self):
        """計算三科的平均分數"""
        return (self.chinese + self.english + self.math) / 3


if __name__ == "__main__":
    # 建立一個學生實例
    student = Student(85, 90, 88)

    # 輸出學生成績
    print(
        f"學生成績：國文 {student.chinese} 分，英文 {student.english} 分，數學 {student.math} 分"
    )

    # 計算並輸出平均分數
    avg = student.average()
    print(f"平均分數：{avg:.2f} 分")
