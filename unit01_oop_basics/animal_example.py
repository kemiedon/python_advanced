# ============================================================================
# 範例 1：基本類別 - 類別定義、建構子、方法、物件建立
# ============================================================================

print("=" * 70)
print("範例 1：基本類別 - 類別定義與物件建立")
print("=" * 70)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} 發出聲音")


# 建立動物實例
animal = Animal("小動物")

print("\n--- 建立物件並呼叫方法 ---")
animal.speak()  # 小動物 發出聲音

print("\n")

# ============================================================================
# 範例 2：繼承與方法覆寫 - 子類覆寫父類方法
# ============================================================================

print("=" * 70)
print("範例 2：繼承與方法覆寫（多型基礎）")
print("=" * 70)


class Dog(Animal):
    def speak(self):
        print(f"{self.name}：汪汪！")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}：喵喵！")


# 建立子類實例
dog = Dog("柴犬")
cat = Cat("波斯貓")

print("\n--- 不同子類的 speak() 方法 ---")
dog.speak()  # 柴犬：汪汪！
cat.speak()  # 波斯貓：喵喵！

print("\n--- 多型示範：用同一個迴圈呼叫不同行為 ---")
animals = [animal, dog, cat]
for ani in animals:
    ani.speak()

print("\n")

# ============================================================================
# 範例 3：封裝 - 使用私有屬性與安全的方法存取
# ============================================================================

print("=" * 70)
print("範例 3：封裝 - 私有屬性與安全的存取方式")
print("=" * 70)


class DogWithEncapsulation(Dog):
    def __init__(self, name, weight):
        super().__init__(name)
        self.__weight = weight

    def eat(self, food_weight):
        if food_weight <= 0:
            print("  食物重量必須大於 0")
            return
        self.__weight += food_weight * 0.2

    def get_info(self):
        return f"{self.name} 現在體重是 {self.__weight} 公斤"


dog_encap = DogWithEncapsulation("小黑", 10)

print("\n--- 初始狀態 ---")
print(dog_encap.get_info())  # 小黑 現在體重是 10 公斤

print("\n--- ✅ 正確方式：使用 eat() 方法 ---")
dog_encap.eat(5)  # 進食 5 公斤食物
print(dog_encap.get_info())  # 小黑 現在體重是 11.0 公斤（增加 5 * 0.2）

print("\n--- ❌ 不建議的方式：試圖直接修改私有屬性 ---")
print("  嘗試執行: dog_encap.__weight = 999")
dog_encap.__weight = 999  # 這會建立一個新屬性，不會修改真正的 __weight
print(f"  結果: {dog_encap.get_info()}")
print("  說明：仍然是 11.0，因為真正的 __weight 沒有被修改")

print("\n")

# ============================================================================
# 範例 4：擴展父類 - 為 Animal 加入新方法，子類添加特色行為
# ============================================================================

print("=" * 70)
print("範例 4：擴展父類 - 新增方法與多個子類的特色")
print("=" * 70)


class AnimalExpanded(Animal):
    def eat(self):
        print(f"{self.name} 正在進食")

    def sleep(self):
        print(f"{self.name} 正在睡覺")


class DogExpanded(AnimalExpanded):
    def bark(self):
        print(f"{self.name} 說：汪汪！")


class CatExpanded(AnimalExpanded):
    def meow(self):
        print(f"{self.name} 說：喵喵！")


class BirdExpanded(AnimalExpanded):
    def fly(self):
        print(f"{self.name} 正在飛行")


# 建立各類型動物的實例
print("\n--- 建立不同動物的實例 ---")
dog_exp = DogExpanded("小黑")
cat_exp = CatExpanded("小花")
bird_exp = BirdExpanded("小綠")

print("\n--- 狗的行為：繼承的方法 + 自己的特色 ---")
dog_exp.eat()  # 來自 AnimalExpanded - 小黑 正在進食
dog_exp.sleep()  # 來自 AnimalExpanded - 小黑 正在睡覺
dog_exp.bark()  # Dog 自己的特色 - 小黑 說：汪汪！

print("\n--- 貓的行為：繼承的方法 + 自己的特色 ---")
cat_exp.eat()  # 來自 AnimalExpanded - 小花 正在進食
cat_exp.meow()  # Cat 自己的特色 - 小花 說：喵喵！

print("\n--- 鳥的行為：繼承的方法 + 自己的特色 ---")
bird_exp.eat()  # 來自 AnimalExpanded - 小綠 正在進食
bird_exp.fly()  # Bird 自己的特色 - 小綠 正在飛行

print("\n")

# ============================================================================
# 範例 5：進階多型 - 為基類加入 move() 方法，子類覆寫實現多型
# ============================================================================

print("=" * 70)
print("範例 5：進階多型 - 統一介面的多樣化實現")
print("=" * 70)


class AnimalWithMove(AnimalExpanded):
    def move(self):
        print(f"{self.name} 正在移動")


class DogWithMove(AnimalWithMove):
    def move(self):
        print(f"{self.name}：在地上跑步")


class CatWithMove(AnimalWithMove):
    def move(self):
        print(f"{self.name}：優雅地走動")


class FishWithMove(AnimalWithMove):
    def move(self):
        print(f"{self.name}：在水裡游泳")


class BirdWithMove(AnimalWithMove):
    def move(self):
        print(f"{self.name}：在天空翱翔")


# 建立各種動物
print("\n--- 多型示範：統一調用 move() 方法，卻有不同行為 ---")
animals_with_move = [
    DogWithMove("小黑"),
    CatWithMove("小花"),
    FishWithMove("金魚"),
    BirdWithMove("小綠"),
    AnimalWithMove("未知動物"),
]

for animal in animals_with_move:
    animal.move()

print("\n")

# ============================================================================
# 總結與重要概念
# ============================================================================

print("=" * 70)
print("OOP 核心概念總結")
print("=" * 70)

summary = """
1. 類別（Class）與物件（Object）
   - 類別是模板，物件是根據模板建立的實例
   - 每個物件有自己的屬性和可以調用的方法

2. 方法與初始化
   - __init__() 是建構子，在建立物件時自動執行
   - 方法是類別內部的函式，用 self 參數存取物件的屬性

3. 繼承（Inheritance）
   - 子類可以繼承父類的屬性和方法
   - 子類可以覆寫（override）父類的方法以改變行為
   - 使用 super() 呼叫父類方法

4. 多型（Polymorphism）
   - 不同物件對同一方法有不同的行為
   - 允許編寫更通用、靈活的程式碼
   - 基於繼承和方法覆寫實現

5. 封裝（Encapsulation）
   - 使用私有屬性（__name）隱藏實現細節
   - 提供公開的方法作為安全的存取介面
   - 保護資料完整性

6. 實務應用
   - 物件導向使程式碼更容易組織、維護和重用
   - 大型專案中能有效管理複雜性
   - 通過繼承和多型減少程式碼重複
"""

print(summary)
