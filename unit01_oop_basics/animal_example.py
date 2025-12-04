# 單元 1：物件導向基礎（OOP）
# Python OOP 基本範例


class Animal:
    """動物類別 - 基本的物件導向示範"""

    def __init__(self, name):
        """初始化動物物件"""
        self.name = name

    def speak(self):
        """發出聲音"""
        print(f"{self.name} 發出聲音")


class Dog(Animal):
    """狗類別 - 繼承自 Animal，覆寫 speak 方法"""

    def speak(self):
        """狗的叫聲"""
        print(f"{self.name}：汪汪！")


class Cat(Animal):
    """貓類別 - 繼承自 Animal，覆寫 speak 方法"""

    def speak(self):
        """貓的叫聲"""
        print(f"{self.name}：喵喵！")


if __name__ == "__main__":
    print("=== OOP 基本範例 ===\n")

    # 建立動物實例
    animal = Animal("小動物")
    dog = Dog("柴犬")
    cat = Cat("波斯貓")

    # 呼叫方法
    animal.speak()  # 小動物 發出聲音
    dog.speak()  # 柴犬：汪汪！
    cat.speak()  # 波斯貓：喵喵！

    print("\n=== 示範多型 ===\n")

    # 使用相同介面，不同行為
    animals = [animal, dog, cat]
    for ani in animals:
        ani.speak()
