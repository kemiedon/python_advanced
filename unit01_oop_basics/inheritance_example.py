# OOP 進階 - 範例 1: 繼承與覆寫

# 父類別：定義共用邏輯
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"大家好，我是{self.grade}年級的{self.name}。")


# 子類別：外國學生，覆寫 introduce() 方法
class ForeignStudent(Student):
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am in grade {self.grade}.")


# 多型應用：統一的自我介紹流程
def show_introduction(student):
    """
    接收任何類型的學生物件，呼叫他的 introduce() 方法
    這就是多型：同一個方法名稱，不同的類別執行不同的行為
    """
    student.introduce()


# 主程式
if __name__ == "__main__":
    # 建立本地學生和外國學生
    ming = Student("小明", 3)
    john = ForeignStudent("John", 2)

    # 透過相同的函式呼叫，卻得到不同的輸出
    print("=== 學生自我介紹 ===")
    show_introduction(ming)  # 中文介紹
    show_introduction(john)  # 英文介紹

    print("\n=== 直接呼叫方法 ===")
    ming.introduce()
    john.introduce()
