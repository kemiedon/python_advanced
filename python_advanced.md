# Python 進階課程

## 單元 1：物件導向基礎（OOP）

### 什麼是物件導向?

物件導向就是「把程式當成一堆會互動的東西（物件）組合起來」，而不是只是一連串從上到下跑的指令。

### 為什麼要用物件導向?

* 把複雜的程式拆成一個一個物件，較容易分工、維護和擴充，例如遊戲裡有「玩家」、「怪物」、「道具」等物件，各自負責自己的事情。
* 修改時通常只改其中一個類別，不用把整支程式翻來翻去，所以程式更好讀、比較不容易改壞其他地方。

### 類別和物件：動物種類 vs. 個別動物

類別（Class）像「動物種類」。
例如: Animal（動物）、Dog（狗）、Cat（貓），類別裡會定義這一類動物的「特徵」和「會做的事」。
物件（Object）就是一隻一隻真正的動物。
例如:「小黑這隻狗」、「小花這隻貓」，它們都是從 Dog 或 Cat 這個類別生出來，各自有自己的名字、年齡、體重。

### 屬性和方法：長相 vs. 行為

屬性（Attribute）就是動物的「資料」。
例如:名字、顏色、年齡、體重，程式裡會寫成 name、color、age、weight 等欄位。
方法（Method）就是動物的「行為」。
例如: eat() 吃東西、sleep() 睡覺、move() 移動、bark() 叫聲，代表這個類別的動物可以做什麼事。

#### Python OOP 基本範例

偽代碼示範:

```
類別：動物（Animal）
    屬性：名字
    方法：發出聲音

類別：狗（Dog），繼承自動物
    方法：發出聲音（覆寫）

# 建立動物實例
小動物 = 動物("小動物")
柴犬 = 狗("柴犬")

# 呼叫方法
小動物.發出聲音()   # 小動物 發出聲音
柴犬.發出聲音()     # 柴犬：汪汪！
```

真實程式:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} 發出聲音")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}：汪汪！")

a = Animal("小動物")
d = Dog("柴犬")

a.speak()   # 小動物 發出聲音
d.speak()   # 柴犬：汪汪！
```

**範例檔案：** `unit01_oop_basics/animal_example.py`

### 練習題

#### 練習 1：基礎類別設計

建立一個 Student 類別來管理學生的成績資料。

**任務：**

```
1. 建立一個名為 Student 的類別
2. 屬性：三科成績（例如國文、英文、數學）
3. 方法：計算平均分數的 average() 方法
4. 建立一個學生實例，輸入成績並計算平均值
```

**期望輸出：**

```
學生成績：國文 85 分，英文 90 分，數學 88 分
平均分數：87.67 分
```

#### 練習 2：類別屬性設計

設計一個「洗衣機」類別來表示不同的洗衣機型號。

**任務：**

```
1. 建立一個名為 WashingMachine 的類別
2. 屬性：brand（品牌）、capacity（容量，單位：公斤）
3. 方法：display_info() 方法，顯示「品牌：XX，容量：XX 公斤」
4. 建立兩個不同品牌的洗衣機實例並呼叫 display_info()
```

**期望輸出：**

```
品牌：LG，容量：8 公斤
品牌：三星，容量：10 公斤
```

**練習檔案：**

* `unit01_oop_basics/exercise01_student_grade.py`
* `unit01_oop_basics/exercise02_washing_machine.py`

### 封裝：動物自己管理身體狀態

- 外面的人不會直接「把動物的體重改成 100 公斤」，而是「給牠很多食物」，牠吃多了自然會變胖；也就是說，真正改變體重的是「吃東西」這個行為，而不是外部直接硬改數值。
- 封裝（Encapsulation）就是物件把「體重怎麼變、健康怎麼計算」這些細節藏起來，只提供像 eat(food) 這種安全的方法讓外界操作，避免亂改內部資料造成錯誤。

```python
class AnimalWithEncapsulation:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def eat(self, food_weight):
        if food_weight <= 0:
            print("食物重量必須大於 0")
            return
        self.__weight += food_weight * 0.2

    def get_info(self):
        return f"{self.__name} 現在體重是 {self.__weight} 公斤"


dog_encap = AnimalWithEncapsulation("小黑", 10)

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
```

### 繼承：從「動物」延續的物種「狗、貓、鳥」

- 可以先定義一個 Animal 類別，裡面放所有動物共有的屬性（name、age）和行為（eat()、sleep()、move()）。
- 然後 Dog、Cat、Bird 這些類別「繼承（Inheritance）Animal」，自動擁有吃和睡的功能，再加上各自的特色，例如 Dog 多了 bark()、Bird 多了 fly()。

```python
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

print("\n")

```

### 多型：同樣是 move()，表現卻不同

- 在程式裡，可以只寫一個 move() 方法名稱，但不同動物可以「用自己的方式移動」：Dog 的 move() 是用跑的、Bird 的 move() 是用飛的、Fish 的 move() 是用游的。
- 多型（Polymorphism）就是主程式只管呼叫 animal.move()，不管這是狗、貓還是鳥，實際執行時會跑到各自類別裡的 move() 實作，讓同一個指令可以有不同表現。

```python

animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()   
# 同樣呼叫 move()，實際表現依物件類別而變

# 輸出：
# Dog runs
# Bird flies
# Fish swims

```

## 物件導向觀念對照表（以動物為例）

| 觀念               | 簡單定義                                                     | 在動物世界的例子                                       | 在程式裡大概長什麼樣子                |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------- |
| 類別 Class         | 一種「種類／設計圖」，定義這一類東西的共同特徵與能力。       | Animal、Dog、Cat 這些「動物種類」。                    | `class Animal { ... }`              |
| 物件 Object        | 從類別生出來的「實體」，真的存在的一個個東西。               | 小黑（那一隻狗）、小花（那一隻貓）。                   | `dog1 = new Dog()`                  |
| 屬性 Attribute     | 描述物件狀態的資料。                                         | 名字、顏色、年齡、體重。                               | `name`, `age`, `weight`         |
| 方法 Method        | 物件可以做的動作或功能。                                     | 吃、睡、移動、叫（eat、sleep、move、bark）。           | `eat()`, `sleep()`, `move()`    |
| 封裝 Encapsulation | 把資料和操作包在物件裡，外面不能直接亂改，只能透過方法存取。 | 不能直接改體重，只能餵食，體重由動物自己依吃多少變化。 | `private weight` 搭配 `eat(food)` |
| 繼承 Inheritance   | 新類別沿用舊類別的屬性與方法，並能再加上自己的。             | Dog、Cat 從 Animal 繼承吃和睡，再各自加上 bark、meow。 | `class Dog extends Animal { ... }`  |
| 多型 Polymorphism  | 同一個介面或方法名，不同類別可以有不同實作。                 | 都是 move()：狗用跑的、鳥用飛的、魚用游的。            | `animal.move()`                     |

#### 練習 3： 綜合應用 - 課程管理系統

設計一個簡單的課程管理系統，讓不同科系學生可以註冊課程、查看成績。

**任務：**

```
1. 建立父類別 Student
   - 屬性：name、courses（已修課程清單，初始為空）
   - 方法：enroll_course(course_name)（選課）
   - 方法：get_courses()（查看課程）

2. 建立子類別 ComputerStudent
   - 覆寫 enroll_course()：只能選「資訊」相關課程
   - 如選到不相關課程，提示「此課程不適合資訊系」

3. 建立子類別 EnglishStudent
   - 覆寫 enroll_course()：只能選「英文」相關課程
   - 如選到不相關課程，提示「此課程不適合英文系」

4. 實例操作：
   - 建立小明（資訊系），選課「Python」（成功）和「莎士比亞」（失敗）
   - 建立小花（英文系），選課「英文文學」（成功）和「資料結構」（失敗）
   - 各自顯示已選課程
```

**期望輸出：**

```
小明選課 Python：成功！
小明選課 莎士比亞：此課程不適合資訊系
小明已修課程：['Python']

小花選課 英文文學：成功！
小花選課 資料結構：此課程不適合英文系
小花已修課程：['英文文學']

```

**練習檔案：**

* `unit01/exercise03_basic_parent_class.py`
* `unit01/exercise04_method_overriding.py`
* `unit01/exercise05_polymorphism.py`
* `unit01/exercise06_course_management.py`

### 常見問題

**Q：self 是什麼？**
→ 就是「我自己」。物件在跟自己說話。

**Q：Class 一定要大寫？**
→ 不是規定，但習慣，大家都這樣寫。

**Q：物件跟變數差在哪？**
→ 物件有「資料 + 功能」。變數只有值。

**Q：繼承就是複製貼上嗎？**
→ 不是，是「延伸」，不用重寫重複的東西。

**Q：多型有什麼好處？**
→ 新增帳戶類型時不用重寫整個系統。

**Q：繼承可以很多層？**
→ 不要太多，超過三層會變可怕。

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請幫我解釋 Python 中的繼承和多型概念
- 請給我一個銀行帳戶系統的繼承範例
- 請幫我實作 SavingAccount 和 CheckingAccount 類別
- 請幫我檢查我的多型實作是否正確

---

## 單元 2：模組化程式開發

### 什麼是「模組」?

在 Python 裡，一個 模組 就是一個副檔名是 .py 的檔案，裡面放相關的一組程式碼，例如一堆計算用的函式。

當程式變大時，不可能所有程式都塞在同一個檔案，所以會把不同功能拆到不同的模組裡，再讓主程式去呼叫。

可以把整個程式想成一個工具箱，模組就像不同的小盒子：螺絲起子放一盒、扳手放一盒，需要什麼就打開那盒來用。

這樣找東西比較快，也不會所有工具混成一團，之後要新增或更換工具也更方便。

### 為什麼要模組化?

* **「重複使用」**：常用的功能（像是計算成績、處理檔案）寫成模組，以後別的專案也能直接 import 來用，不用重寫。
* **「好維護」**：如果成績計算有 bug，只要改那個模組檔案，所有用到它的程式就一起變正確。

### 模組和套件的差別?

模組是「一個檔案」，套件（package）則是「一個資料夾」，裡面可以裝很多模組檔案，用來組成更大的功能集合。

比方說一個專案資料夾裡，有好幾個處理不同功能的模組檔案，就可以一起當成一個套件來管理。

### 練習題

#### 模組化實作練習：做三明治

請依下列步驟完成一個「三明治製作」的模組化程式：

1. 建立或使用以下檔案：

   - `exercise01_bread.py`：實作 `cut_bread()`（切麵包）
   - `exercise02_lettuce.py`：實作 `prepare_lettuce()`（準備生菜）
   - `exercise03_sandwich.py`：主程式，匯入並呼叫前兩者以組合三明治
2. 在 `exercise03_sandwich.py` 中示範如何呼叫上述函式並在最後印出 `三明治完成！`。
3. 包含 `if __name__ == "__main__"`，以便直接執行測試。

請將檔案放在 `unit02_modularity` 資料夾中，並以 `exercise0X` 命名方式提交練習。

**練習檔案：**

* `unit02_modularity/exercise01_bread.py`
* `unit02_modularity/exercise02_lettuce.py`
* `unit02_modularity/exercise03_sandwich.py`

### 常見問題

**Q：模組能拆多細？**
→ 一個檔案負責一種功能就剛好。

**Q：import 找不到檔？**
→ 大多是路徑或檔名錯了。

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請幫我解釋什麼是模組化和為什麼重要
- 請幫我規劃如何拆分一個大型 Python 專案
- 請給我模組化重構的最佳實踐
- 請幫我檢查 import 語句和模組結構是否正確

---

## 單元 3：Python 內建模組

### 什麼是 Python 內建模組？

內建模組（built-in modules）就是 Python 安裝完後「隨附」的工具箱，你不用再下載，打 `import` 直接就能用。

### 常用 Python 內建模組介紹 & 範例

1. math
   用來做數學運算（例如開根號、取絕對值、三角函數）

```python
import math
print(math.sqrt(16))  # 開根號，輸出 4.0
print(math.pi)        # 圓周率
```

**範例檔案：** `unit03_builtin_modules/example_math.py`

2. random
   隨機數（抽籤、選號碼）

```python
import random
print(random.randint(1, 10))   # 隨機整數 1~10
print(random.choice(['A', 'B', 'C']))  # 隨機選一個
```

**範例檔案：** `unit03_builtin_modules/example_random.py`

3. datetime
   處理時間與日期

```python
import datetime
now = datetime.datetime.now()
print(now)  # 現在時間
print(now.year, now.month, now.day)
```

**範例檔案：** `unit03_builtin_modules/example_datetime.py`

4. os
   跟作業系統互動（像瀏覽檔案、建立資料夾）

```python
import os
print(os.listdir('.'))  # 列出目前資料夾的檔案
os.mkdir('testdir')     # 建立資料夾
```

**範例檔案：** `unit03_builtin_modules/example_os.py`

5. sys
   取得 Python 系統與參數資訊

```python
import sys
print(sys.version)  # Python 版本
print(sys.argv)     # 執行程式時的參數清單
```

**範例檔案：** `unit03_builtin_modules/example_sys.py`

6. json
   讓你可以把字典等資料變成文字（序列化、一樣反過來也行）

```python
import json
data = {'name': 'Amy', 'age': 20}
json_str = json.dumps(data)   # 變成文字
print(json_str)
data2 = json.loads(json_str)  # 變回原本資料型態
print(data2)
```

**範例檔案：** `unit03_builtin_modules/example_json.py`

### 練習題

#### 練習 1：抽獎與分組

使用 `random` 實作抽獎與分組功能：

- 實作 `draw_winner(students)`：從 `students` 清單回傳一名中獎者（使用 `random.choice`）。
- 實作 `make_group(students, n)`：從 `students` 中隨機抽出 `n` 人成為一組（使用 `random.sample`）。
- 實作 `split_into_two(students)`：將 `students` 亂數排序後分成兩組（使用 `random.shuffle`）。

範例輸出：

```
這次抽獎中獎學生是：小美
小組成員： ['Amy', '阿強', '小明']
第一組： ['阿花', '小明', 'John']
第二組： ['小美', 'Amy', '阿強']
```

**範例檔案：** `unit03_builtin_modules/exercise01_random.py`

---

#### 練習 2：數學工具應用

使用 `math` 實作兩個小功能：

- `calc_hypotenuse(a, b)`：回傳直角三角形斜邊長（使用 `math.hypot` 或 sqrt）。
- `angle_to_radian_and_back(deg)`：將角度轉為弳度，計算 sin/cos 並回傳結果（使用 `math.radians`、`math.sin`、`math.cos`）。

期望示範：輸入 (3,4) 得到 5.0；輸入 90 度得到 sin≈1.0。

**範例檔案：** `unit03_builtin_modules/exercise02_math.py`

#### 練習 3：時間與檔名

使用 `datetime` 建立以時間為基礎的檔名與時間顯示：

- `timestamped_filename(prefix)`：回傳 `prefix_YYYYMMDD_HHMMSS.txt` 格式的檔名（使用 `datetime.now()` 與 `strftime`）。
- `print_now()`：印出目前年月日與時間的分別欄位（年/月/日/時/分/秒）。

範例輸出：

```
2025-11-23 14:30:05
filename: report_20251123_143005.txt
```

**範例檔案：** `unit03_builtin_modules/exercise03_datetime.py`

#### 練習 4：檔案系統基本操作

使用 `os` 或 `pathlib` 實作簡單的檔案管理工具：

- `list_files(path)`：列出指定資料夾下所有檔案（使用 `os.listdir` 或 `pathlib.Path.iterdir()`）。
- `ensure_dir(path)`：如果資料夾不存在就建立（使用 `os.makedirs` 或 `Path.mkdir(parents=True, exist_ok=True)`)。
- `group_by_extension(path)`：把目錄下的檔案依副檔名分組並回傳字典（副檔名 -> 檔名清單）。

**範例檔案：** `unit03_builtin_modules/exercise04_filesystem.py`

#### 練習 5：JSON 與系統參數

結合 `json` 與 `sys`：

- 寫一個程式 `save_students.py`，接受命令列參數（`sys.argv`）作為輸入檔名，將學生清單序列化為 JSON 存檔（使用 `json.dump`）。
- 寫一個對應的 `load_students.py`，讀取該 JSON 檔並列印資料。

範例：

```
save_students.py students.json load_students.py students.json
```

**範例檔案：** `unit03_builtin_modules/exercise05_load_students.py`

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請解釋 os、pathlib、datetime、shutil 的用途和區別
- 請給我一個自動分類檔案的完整範例
- 請幫我實作自動改檔名並加日期的功能
- 請幫我檢查檔案操作的程式碼是否正確

---

## 單元 4：閉包 & 裝飾器（@ 的真相）

### 什麼是閉包?（Closure）

**定義**：可以把閉包想成「會記住東西的函式」。一個函式裡面再定義一個小函式，小函式會用到外面那個函式的變數，然後外面那個函式把小函式「return 回去」，這時得到的小函式，就會一直記得那些變數的值。

就算外面的函式早就跑完了、照理說變數應該消失了，但這個小函式還是能用那些變數，因為 Python 幫它把需要的變數「包起來」一起帶走，這一包就是閉包。

**生活比喻:**
想像你去補習班，老師上完一堂課（外層函式結束），但是你筆記裡的重點（變數）會被你帶回家，小抄就是那個「內層函式」，隨時可以打開來用先前記住的內容，這就是閉包的感覺。

所以閉包常拿來做「記住某個設定」的函式，比如先設定好稅率 5%，之後每次把金額丟進去，它都用同一個稅率幫你算，不用每次都再傳 5% 進去。

- **範例**：

```python
def outer(message):
   def inner():
      print("外層變數:", message)
   return inner

say_hello = outer("Hello closure!")
say_hello()  # 輸出：外層變數: Hello closure!
```

---

### 什麼是裝飾器?（Decorator）

**定義**：裝飾器就是「幫函式加功能的工具」，而且「不改動原本的函式裡面程式碼」。寫一個函式 A，專門負責「包住」別的函式，讓別的函式在執行前後，多做一些事情，例如：先印一行「開始執行」、算執行時間、檢查權限等等。

在 Python 裡，用 `@裝飾器名稱` 放在函式上面，就是在說「這個函式要先經過這個裝飾器處理」，像是 `@login_required`、`@app.route('/')` 這種都是裝飾器的用法。

**範例**：

```python
def my_decorator(func):
   def wrapper():
      print("執行前")
      func()
      print("執行後")
   return wrapper

@my_decorator
def say_hi():
   print("Hi, Python!")

say_hi()
```

執行結果：

```
執行前
Hi, Python!
執行後
```

#### 範例檔: 計數器

```python
# closure_counter.py
def make_counter(name):
   count = 0
   def add_one():
      nonlocal count
      count += 1
      print(f"{name} 的計數：{count}")
   return add_one

if __name__ == "__main__":
   alice = make_counter("小明")
   bob = make_counter("小美")
   alice()
   alice()
   bob()
   bob()
```

**範例檔案：** `unit04_closure_decorator/closure_example.py`

下面範例是在示範「用裝飾器統一做登入驗證」，用來「幫函式加上一層登入檢查」的功能。

```python
# require_login.py
from functools import wraps

def require_login(func):
   @wraps(func)
   def wrapper(user, *args, **kwargs):
      if not user:
         print("❌ 請先登入")
         return
      print("✓ 已驗證身份，開始執行")
      return func(user, *args, **kwargs)
   return wrapper

@require_login
def access_system(user):
   print(f"歡迎 {user}，進入系統")

if __name__ == "__main__":
   access_system("小明")
   access_system(None)
```

**範例檔案：** `unit05_closure_decorator/require_login_example.py`

下列範例「帶參數的裝飾器」，用來檢查使用者是不是指定角色（例如 admin），不是的話就擋掉不讓執行。帶參數的裝飾器常用在權限控制、以角色為基礎的存取控制這類情境。

```python
# role_decorator.py
from functools import wraps

def require_role(role):
   def decorator(func):
      @wraps(func)
      def wrapper(user, *args, **kwargs):
         if not user or user.get("role") != role:
            print(f"❌ 需要 {role} 權限")
            return
         return func(user, *args, **kwargs)
      return wrapper
   return decorator

@require_role("admin")
def delete_resource(user):
   print(f"{user['name']} 刪除資源")

if __name__ == "__main__":
   admin = {"name": "小明", "role": "admin"}
   guest = {"name": "小美", "role": "guest"}
   delete_resource(admin)
   delete_resource(guest)
```

**範例檔案：** `unit05_closure_decorator/timeit_example.py`（時間裝飾器範例）

### 練習題

#### 練習 1：購物車的計數器

要求：

- 建立一個閉包函式儲存單一顧客的購物紀錄
- 支持「加商品」、「移除商品」、「查看購物車總額」三個操作
- 確保不同顧客的購物車互不影響

#### 練習 2：銀行提款限制

要求：

- 建立一個裝飾器檢查提款金額是否超過每日限額（$5000）
- 建立另一個裝飾器檢查帳戶餘額是否足夠
- 套用兩個裝飾器到提款函式上

#### 練習 3：API 呼叫的重試機制

要求：

- 建立一個裝飾器，函式執行出錯時自動重試（3 次）
- 每次重試前等待 1 秒
- 顯示重試次數與結果

練習 4：自訂快取裝飾器

要求：

- 建立帶參數的裝飾器 `@cache(timeout=30)` 快取函式結果
- `timeout` 參數控制快取有效時間（秒）
- 快取過期後重新計算
- 顯示「快取命中」或「重新計算」的訊息

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請解釋什麼是閉包和裝飾器
- 請給我一個簡單的閉包計數器範例
- 請幫我實作登入驗證裝飾器
- 請給我計算執行時間的裝飾器實作
- 請幫我理解帶參數的裝飾器如何運作

---

## 單元 5：檔案與資料處理（CSV / JSON / Error）

### 什麼是檔案與資料處理？

在實際應用中，我們經常需要：

- **儲存資料**：將程式產生的資料永久保存
- **讀取資料**：載入先前儲存的資料繼續處理
- **交換資料**：與其他系統或程式分享資料
- **備份資料**：避免資料遺失

Python 提供了豐富的工具來處理各種格式的檔案和資料。

### 生活範例應用

你是班導師，期末要整理全班 40 位學生的成績：

- 用 Excel 手動計算平均分數 → 很慢，容易出錯
- 需要找出前三名學生 → 要一個一個比較
- 要製作成績單給每位學生 → 複製貼上 40 次

**用 Python 可以幫你：**

1. 從 CSV 讀取成績資料（2 秒）
2. 自動計算所有統計數據（1 秒）
3. 排序找出前幾名（0.1 秒）
4. 匯出個人成績單（1 秒）
5. 備份資料到 JSON（1 秒）

總共不到 5 秒！

#### 檔案操作的三種常見情境

1. **文字檔案**：筆記、日記、設定檔

   - 例如：儲存每日學習筆記、讀取設定檔
2. **CSV 檔案**：表格資料（像 Excel）

   - 例如：學生名單、成績表、銷售記錄
3. **JSON 檔案**：結構化資料（網站常用）

   - 例如：使用者資料、設定資料、API 回應

### 基本檔案讀寫

#### 寫入檔案

```python
# 寫入模式（會覆蓋原有內容）
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("今天學了 Python 檔案處理\n")
    f.write("覺得很有趣！\n")
```

#### 讀取檔案

```python
# 讀取模式
with open("diary.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

#### 附加內容

```python
# 附加模式（不會覆蓋，在檔案後面加內容）
with open("diary.txt", "a", encoding="utf-8") as f:
    f.write("下午繼續練習！\n")
```

**範例檔案：** `unit05_file_data_processing/example01_basic_file.py`

### CSV 檔案處理

#### 什麼是 CSV 檔

CSV 是一種「純文字格式」，但裡面的資料長得像表格：一列一列的資料，欄位之間用逗號分開，例如：Name,Age,Gender。
副檔名通常是 .csv，可以用 Excel、Google 試算表打開，也可以用記事本之類的文字編輯器打開, CSV 通用性很高：幾乎所有系統（資料庫、網站後台、統計軟體）都能讀寫 CSV，用來「匯入、匯出資料」超方便。

#### 寫入 CSV

```python
import csv

students = [
    ["姓名", "國文", "英文", "數學"],
    ["小明", "85", "90", "88"],
    ["小美", "92", "87", "95"]
]

with open("students.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(students)
```

#### 讀取 CSV

```python
import csv

with open("students.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

#### 使用字典方式讀取 CSV

```python
import csv

with open("students.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']}：國文 {row['國文']}，英文 {row['英文']}")
```

**範例檔案：** `unit05_file_data_processing/example02_csv_operations.py`

### JSON 處理

JSON 全名是 JavaScript Object Notation，是一種「用文字描述資料結構」的格式，副檔名通常是 .json

JSON 是網路上最常用的資料交換格式，可以把它想成「有階層結構的資料筆記本」，用一種固定格式把資料寫成文字，讓人和程式都看得懂、都能互相交換

#### Python 資料轉 JSON

```python
import json

student = {
    "name": "小明",
    "age": 20,
    "grades": {"國文": 85, "英文": 90}
}

# 轉成 JSON 字串
json_str = json.dumps(student, ensure_ascii=False, indent=2)
print(json_str)
```

#### JSON 轉 Python 資料

```python
import json

json_str = '{"name": "小美", "age": 19}'
student = json.loads(json_str)

print(student["name"])  # 小美
```

#### 寫入 JSON 檔案

```python
import json

students = [
    {"name": "小明", "age": 20},
    {"name": "小美", "age": 19}
]

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)
```

#### 讀取 JSON 檔案

```python
import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    print(f"{student['name']} ({student['age']} 歲)")
```

**範例檔案：** `unit05_file_data_processing/example03_json_operations.py`

### 錯誤處理（try-except）

在寫程式的過程中，尤其是處理檔案時，很多事情可能出錯：檔案不存在、格式錯誤、權限不足等。

#### 處理檔案不存在

```python
try:
    with open("不存在的檔案.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("✗ 檔案不存在")
```

#### 處理資料格式錯誤

```python
data = ["85", "90", "abc", "88"]

for item in data:
    try:
        score = int(item)
        print(f"✓ 成功轉換：{item} → {score}")
    except ValueError:
        print(f"✗ 無法轉換：{item}")
```

#### 處理多種錯誤

```python
try:
    with open("data.txt", "r") as f:
        number = int(f.read())
except FileNotFoundError:
    print("✗ 檔案不存在")
except ValueError:
    print("✗ 資料格式錯誤")
except Exception as e:
    print(f"✗ 未預期的錯誤：{e}")
finally:
    print("→ 無論成功或失敗都會執行")
```

**重點整理：**

- `try-except` 捕捉錯誤，避免程式崩潰
- `FileNotFoundError`：檔案不存在
- `ValueError`：資料格式轉換錯誤
- `finally`：無論如何都會執行（用於清理資源）

**範例檔案：** `unit05_file_data_processing/example04_error_handling.py`

### 資料驗證與清理

資料驗證是在「資料進來的當下」檢查：有沒有填、格式對不對、範圍合不合理，例如年齡必須在 0～120、學生年級只能是 1–3 年級、Email 一定要有 @。
資料清理是在「資料已經收集完之後」再回頭整理，找出錯誤、缺失或不一致的地方，並做修正或刪除。

處理真實資料時，經常會遇到「髒資料」，例如：

- 缺漏值（空白、None）
- 格式錯誤（應該是數字卻是文字）
- 超出範圍（年齡 -5 歲、分數 150 分）

因此，資料驗證是先檢查資料合不合理，資料清理是把已經收集到的髒資料整理乾淨，兩個都是為了讓分析結果可信。

#### 驗證資料範例

```python
def validate_score(score):
    """驗證分數是否有效"""
    if not isinstance(score, (int, float)):
        raise TypeError("分數必須是數字")
    if score < 0 or score > 100:
        raise ValueError("分數必須在 0-100 之間")
    return True

# 使用驗證
test_scores = [85, 120, -10, "abc"]

for score in test_scores:
    try:
        validate_score(score)
        print(f"✓ {score} 是有效分數")
    except (TypeError, ValueError) as e:
        print(f"✗ {score}：{e}")
```

#### 清理資料範例

```python
import csv

def clean_student_data(input_file, output_file):
    """清理學生資料並輸出"""
    clean_rows = []

    with open(input_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # 檢查姓名不為空
            if not row["姓名"].strip():
                continue

            # 修正年齡（如果無效就設為預設值）
            try:
                age = int(row["年齡"])
                if age < 15 or age > 30:
                    age = 20
            except ValueError:
                age = 20

            # 修正成績（限制在 0-100）
            try:
                score = int(row["成績"])
                score = max(0, min(100, score))
            except ValueError:
                continue  # 跳過無效成績

            clean_rows.append({
                "姓名": row["姓名"],
                "年齡": age,
                "成績": score
            })

    # 寫入清理後的資料
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["姓名", "年齡", "成績"])
        writer.writeheader()
        writer.writerows(clean_rows)
```

**範例檔案：** `unit05_file_data_processing/example05_data_cleaning.py`

### 練習題

#### 練習 1：讀寫文字檔案

建立日記系統，實作以下功能：

- `create_diary(filename, content)`：建立日記檔案
- `read_diary(filename)`：讀取日記內容
- `append_diary(filename, content)`：追加新內容

**期望效果：**

```python
create_diary("my_diary.txt", "今天學了 Python")
append_diary("my_diary.txt", "晚上繼續練習")
read_diary("my_diary.txt")
# 輸出：
# 今天學了 Python
# 晚上繼續練習
```

**練習檔案：** `unit05_file_data_processing/exercise01_read_write.py`

#### 練習 2：處理 CSV 成績資料

建立成績處理系統：

- `create_grade_csv(filename)`：產生測試用的成績 CSV
- `calculate_averages(filename)`：計算每位學生平均分數
- `find_top_students(filename, n)`：找出前 n 名學生
- `export_with_rank(input_file, output_file)`：輸出包含排名的新 CSV

**期望輸出：**

```
前 3 名學生：
第 1 名：小美 （91.33 分）
第 2 名：小華 （90.67 分）
第 3 名：小明 （87.67 分）
```

**練習檔案：** `unit05_file_data_processing/exercise02_csv_grade.py`

#### 練習 3：JSON 資料備份與還原

建立資料備份系統：

- `create_student_data()`：產生學生資料
- `backup_to_json(data, filename)`：備份到 JSON
- `restore_from_json(filename)`：從 JSON 還原
- `search_student(data, name)`：搜尋學生資料

**應用情境：**

程式意外關閉或資料遺失時，可以從 JSON 備份檔快速還原。

**練習檔案：** `unit05_file_data_processing/exercise03_json_backup.py`

#### 練習 4：資料驗證與錯誤處理

建立健壯的資料處理系統：

- `validate_student_data(data)`：驗證資料格式
- `safe_read_csv(filename)`：安全讀取 CSV（處理各種錯誤）
- `process_grades_with_validation(filename)`：處理成績並驗證

**驗證規則：**

- 姓名：不能為空
- 年齡：15-30 之間的整數
- 成績：0-100 之間的數字

**期望行為：**

```
✓ 第 2 行：小明 - 資料有效
✗ 第 3 行資料無效：
    - 姓名為空
✗ 第 4 行資料無效：
    - 年齡 'abc' 不是有效數字
✗ 第 5 行資料無效：
    - 成績 150 超出範圍
```

**練習檔案：** `unit05_file_data_processing/exercise04_data_validation.py`

#### 練習 5：綜合應用 - 學生成績管理系統

整合所有學到的技術，建立完整的管理系統：

**功能需求：**

1. 從 CSV 載入學生資料
2. 新增、修改、刪除學生
3. 計算統計資料（平均、最高、最低）
4. 搜尋與篩選學生
5. 資料驗證與錯誤處理
6. 自動備份到 JSON
7. 匯出成績報表到 CSV

**期望功能展示：**

```python
system = StudentGradeSystem()
system.load_from_csv("students.csv")
system.add_student("S005", "小華", 95, 89, 92)
system.update_student("S001", chinese=90)
system.delete_student("S003")
system.display_statistics()
system.backup_to_json()
system.export_to_csv("report.csv")
```

**練習檔案：** `unit05_file_data_processing/exercise05_integrated_system.py`

### 常見問題

**Q：為什麼要用 `with open()` 而不是 `f = open()`？**
→ `with` 會自動關閉檔案，即使出錯也會正確關閉，避免資源洩漏。

**Q：CSV 和 JSON 有什麼差別？**
→ CSV 適合表格資料（像 Excel），JSON 適合結構化、巢狀資料（像網站資料）。

**Q：什麼時候需要 try-except？**
→ 處理檔案、網路、使用者輸入等「可能出錯」的操作時都應該用。

**Q：如何選擇檔案格式？**
→ 簡單表格用 CSV、複雜結構用 JSON、純文字用 .txt。

**Q：資料清理要做到什麼程度？**
→ 確保「不會讓程式崩潰」+「結果有意義」就夠了，完美是不可能的。

### 實務應用場景

1. **學校成績管理**：匯入學生成績、計算統計、產生報表
2. **商店銷售分析**：讀取銷售記錄、分析趨勢、產生圖表
3. **資料備份系統**：定期將資料備份成 JSON，避免遺失
4. **日誌記錄**：程式運行時自動記錄操作日誌到文字檔
5. **設定檔管理**：讀取 JSON 設定檔，調整程式行為

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請給我一個讀寫 CSV 檔案的完整範例
- 請幫我實作處理缺漏資料的邏輯
- 請給我 JSON 序列化和反序列化的範例
- 請幫我實作 try-except 錯誤處理的最佳實踐
- 請幫我檢查資料處理程式碼中的潛在錯誤
- 請解釋 with open() 和普通 open() 的差異
- 請幫我設計一個資料驗證函式
- 請給我一個完整的 CSV 到 JSON 轉換範例

---

## 單元 6：關聯式資料庫（SQL + SQLite）

### 為什麼要學資料庫？

**生活情境：**
想像你是學校的教務人員，需要管理數千位學生的成績資料。

- **用 CSV？** 當你想查詢「平均成績 > 80 分的學生有誰」時，需要寫程式逐行讀取、計算，很麻煩。
- **用資料庫？** 只要一行 SQL 指令：`SELECT * FROM students WHERE avg_score > 80`，秒出結果！

**資料庫的優勢：**

- ✅ **高效查詢**：快速找到符合條件的資料
- ✅ **資料完整性**：避免重複、確保關聯正確
- ✅ **多人存取**：同時有很多人查詢、修改資料
- ✅ **交易安全**：確保資料更新的完整性（要嘛全部成功，要嘛全部取消）

### 範例：學生成績管理

**情境：**

- 學校有很多學生，每個學生有多科成績
- 需要計算平均分數、找出最高分、統計不及格人數
- 需要快速查詢「某科目平均分數」、「某學生所有成績」

**傳統做法（CSV）：**

```python
# 讀取整個檔案
import csv
with open('grades.csv') as f:
    data = list(csv.DictReader(f))

# 手動計算平均
total = sum(float(row['score']) for row in data if row['subject'] == '數學')
count = len([row for row in data if row['subject'] == '數學'])
average = total / count
```

**資料庫做法（SQL）：**

```python
import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 一行指令搞定
cursor.execute("SELECT AVG(score) FROM grades WHERE subject='數學'")
average = cursor.fetchone()[0]
```

**差別：**

- CSV 需要讀取全部資料、寫程式計算
- SQL 直接下指令，資料庫自動計算
- 資料越多，SQL 優勢越明顯！

### 程式範例

#### 範例 1：SQLite 基本操作

**目標：** 學習如何建立資料庫、建立資料表、進行基本的 CRUD 操作。

**情境：** 建立學生資料庫，記錄學生的基本資料。

```python
import sqlite3
from datetime import datetime


def create_database():
    """建立資料庫和資料表"""
    # 連接資料庫（如果不存在會自動建立）
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # 建立學生資料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            created_at TEXT
        )
    ''')

    conn.commit()
    print("✓ 資料表建立成功")
    return conn


def insert_student(conn, student_id, name, age, email):
    """插入學生資料"""
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO students (student_id, name, age, email, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (student_id, name, age, email, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        conn.commit()
        print(f"✓ 已新增學生：{name}")
    except sqlite3.IntegrityError:
        print(f"✗ 學號 {student_id} 已存在")


def select_all_students(conn):
    """查詢所有學生"""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')

    students = cursor.fetchall()

    print("\n所有學生資料：")
    print("-" * 70)
    for student in students:
        print(f"ID: {student[0]}, 學號: {student[1]}, 姓名: {student[2]}, "
              f"年齡: {student[3]}, Email: {student[4]}")


def update_student_email(conn, student_id, new_email):
    """更新學生 Email"""
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE students
        SET email = ?
        WHERE student_id = ?
    ''', (new_email, student_id))

    conn.commit()
    print(f"✓ 已更新學號 {student_id} 的 Email")


def delete_student(conn, student_id):
    """刪除學生"""
    cursor = conn.cursor()

    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))

    conn.commit()
    print(f"✓ 已刪除學號 {student_id} 的學生")


# 主程式
conn = create_database()

# 新增資料
insert_student(conn, 'S001', '王小明', 20, 'ming@example.com')
insert_student(conn, 'S002', '李小華', 21, 'hua@example.com')
insert_student(conn, 'S003', '張大同', 19, 'tong@example.com')

# 查詢資料
select_all_students(conn)

# 更新資料
update_student_email(conn, 'S001', 'newming@example.com')

# 刪除資料
delete_student(conn, 'S003')

# 再次查詢
select_all_students(conn)

conn.close()
```

**範例檔案：** `unit06_sql_database/example01_basic_sqlite.py`

#### 範例 2：CRUD 操作（類別封裝）

**目標：** 使用類別封裝資料庫操作，提高程式碼的可讀性和重用性。

```python
import sqlite3
from datetime import datetime


class StudentDatabase:
    """學生資料庫管理類別"""

    def __init__(self, db_name='students.db'):
        """初始化資料庫連接"""
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """建立資料表"""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                age INTEGER,
                major TEXT,
                created_at TEXT
            )
        ''')
        self.conn.commit()

    def add(self, student_id, name, age, major):
        """新增學生（Create）"""
        cursor = self.conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO students (student_id, name, age, major, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (student_id, name, age, major, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

            self.conn.commit()
            print(f"✓ 成功新增學生：{name}")
            return True
        except sqlite3.IntegrityError:
            print(f"✗ 學號 {student_id} 已存在")
            return False

    def get_all(self):
        """取得所有學生（Read）"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()

    def get_by_id(self, student_id):
        """依學號查詢學生（Read）"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        return cursor.fetchone()

    def update(self, student_id, **kwargs):
        """更新學生資料（Update）"""
        cursor = self.conn.cursor()

        # 動態建立 UPDATE 語句
        fields = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values()) + [student_id]

        cursor.execute(f'''
            UPDATE students
            SET {fields}
            WHERE student_id = ?
        ''', values)

        self.conn.commit()
        print(f"✓ 成功更新學號 {student_id} 的資料")

    def delete(self, student_id):
        """刪除學生（Delete）"""
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.conn.commit()
        print(f"✓ 成功刪除學號 {student_id}")

    def display_all(self):
        """顯示所有學生"""
        students = self.get_all()

        if not students:
            print("目前沒有學生資料")
            return

        print("\n" + "="*80)
        print(f"{'ID':<5} {'學號':<10} {'姓名':<10} {'年齡':<5} {'科系':<15} {'建立時間':<20}")
        print("="*80)

        for student in students:
            print(f"{student[0]:<5} {student[1]:<10} {student[2]:<10} {student[3]:<5} "
                  f"{student[4]:<15} {student[5]:<20}")

        print("="*80)

    def close(self):
        """關閉資料庫連接"""
        self.conn.close()
```

**範例檔案：** `unit06_sql_database/example02_crud_operations.py`

#### 範例 3：SQL 查詢範例

**目標：** 學習各種 SQL 查詢語法，包含條件篩選、排序、分組、聚合函數等。

```python
import sqlite3


def create_sample_data():
    """建立範例資料"""
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # 建立學生資料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            class TEXT,
            score INTEGER
        )
    ''')

    # 插入測試資料
    students = [
        (1, '王小明', 18, 'A班', 85),
        (2, '李小華', 19, 'A班', 92),
        (3, '張大同', 18, 'B班', 78),
        (4, '陳小美', 19, 'B班', 88),
        (5, '林大強', 18, 'A班', 76),
        (6, '黃小芳', 19, 'C班', 95),
        (7, '劉小軒', 18, 'C班', 82),
        (8, '吳小龍', 19, 'B班', 90)
    ]

    cursor.executemany('''
        INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?, ?)
    ''', students)

    conn.commit()
    return conn


# 1. WHERE 條件查詢
conn = create_sample_data()
cursor = conn.cursor()

print("【查詢成績 > 85 的學生】")
cursor.execute("SELECT name, score FROM students WHERE score > 85")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}分")

# 2. ORDER BY 排序
print("\n【按成績由高到低排序】")
cursor.execute("SELECT name, score FROM students ORDER BY score DESC")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}分")

# 3. LIMIT 限制筆數
print("\n【成績前 3 名】")
cursor.execute("SELECT name, score FROM students ORDER BY score DESC LIMIT 3")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}分")

# 4. GROUP BY 分組統計
print("\n【各班平均成績】")
cursor.execute("""
    SELECT class, AVG(score) as avg_score, COUNT(*) as student_count
    FROM students
    GROUP BY class
""")
for row in cursor.fetchall():
    print(f"{row[0]}: 平均 {row[1]:.2f}分，共 {row[2]} 人")

# 5. HAVING 條件
print("\n【平均成績 > 80 的班級】")
cursor.execute("""
    SELECT class, AVG(score) as avg_score
    FROM students
    GROUP BY class
    HAVING AVG(score) > 80
""")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]:.2f}分")

conn.close()
```

**範例檔案：** `unit06_sql_database/example03_query_examples.py`

#### 範例 4：多表 JOIN 查詢

**目標：** 學習如何使用 JOIN 連接多個資料表，進行複雜查詢。

**情境：** 學生選課系統，需要查詢「誰選了哪些課」、「哪門課有哪些學生」等資訊。

```python
import sqlite3


def create_course_system():
    """建立選課系統資料庫"""
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    # 學生資料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT
        )
    ''')

    # 課程資料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id TEXT PRIMARY KEY,
            course_name TEXT,
            credits INTEGER
        )
    ''')

    # 選課資料表（關聯表）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            course_id TEXT,
            grade INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    ''')

    # 插入測試資料
    students = [
        ('S001', '王小明'),
        ('S002', '李小華'),
        ('S003', '張大同')
    ]

    courses = [
        ('CS101', 'Python 程式設計', 3),
        ('MATH201', '微積分', 4),
        ('ENG101', '英文', 2)
    ]

    enrollments = [
        ('S001', 'CS101', 85),
        ('S001', 'MATH201', 78),
        ('S002', 'CS101', 92),
        ('S002', 'ENG101', 88),
        ('S003', 'MATH201', 95),
        ('S003', 'ENG101', 82)
    ]

    cursor.executemany('INSERT OR REPLACE INTO students VALUES (?, ?)', students)
    cursor.executemany('INSERT OR REPLACE INTO courses VALUES (?, ?, ?)', courses)
    cursor.executemany('INSERT OR REPLACE INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)', enrollments)

    conn.commit()
    return conn


conn = create_course_system()
cursor = conn.cursor()

# 1. INNER JOIN：查詢學生的選課記錄
print("【學生選課記錄】")
cursor.execute("""
    SELECT students.name, courses.course_name, enrollments.grade
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.student_id
    INNER JOIN courses ON enrollments.course_id = courses.course_id
""")

for row in cursor.fetchall():
    print(f"{row[0]} 選修 {row[1]}，成績：{row[2]}分")

# 2. GROUP BY：每個學生的平均成績
print("\n【學生平均成績】")
cursor.execute("""
    SELECT students.name, AVG(enrollments.grade) as avg_grade
    FROM students
    INNER JOIN enrollments ON students.student_id = enrollments.student_id
    GROUP BY students.student_id
""")

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]:.2f}分")

# 3. 複雜查詢：找出修「Python 程式設計」且成績 > 85 的學生
print("\n【Python 課程成績 > 85 的學生】")
cursor.execute("""
    SELECT students.name, enrollments.grade
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.student_id
    INNER JOIN courses ON enrollments.course_id = courses.course_id
    WHERE courses.course_name = 'Python 程式設計' AND enrollments.grade > 85
""")

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}分")

conn.close()
```

**範例檔案：** `unit06_sql_database/example04_join_tables.py`

#### 範例 5：交易處理（Transaction）

**目標：** 學習如何使用交易確保資料的一致性。

**情境：** 銀行轉帳系統，A 帳戶轉錢給 B 帳戶，必須確保「要嘛都成功，要嘛都失敗」。

```python
import sqlite3


def create_bank_database():
    """建立銀行帳戶資料庫"""
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id TEXT PRIMARY KEY,
            name TEXT,
            balance REAL
        )
    ''')

    # 初始資料
    accounts = [
        ('A001', '王小明', 10000.0),
        ('A002', '李小華', 5000.0)
    ]

    cursor.executemany('INSERT OR REPLACE INTO accounts VALUES (?, ?, ?)', accounts)
    conn.commit()

    return conn


def transfer_money(conn, from_account, to_account, amount):
    """轉帳（使用交易）"""
    cursor = conn.cursor()

    try:
        # 開始交易
        conn.execute('BEGIN')

        # 檢查餘額
        cursor.execute('SELECT balance FROM accounts WHERE account_id = ?', (from_account,))
        balance = cursor.fetchone()[0]

        if balance < amount:
            raise ValueError(f"餘額不足！目前餘額：{balance}")

        # 扣款
        cursor.execute('''
            UPDATE accounts
            SET balance = balance - ?
            WHERE account_id = ?
        ''', (amount, from_account))

        # 入帳
        cursor.execute('''
            UPDATE accounts
            SET balance = balance + ?
            WHERE account_id = ?
        ''', (amount, to_account))

        # 提交交易
        conn.commit()
        print(f"✓ 轉帳成功：從 {from_account} 轉 {amount} 元到 {to_account}")
        return True

    except Exception as e:
        # 發生錯誤，回滾交易
        conn.rollback()
        print(f"✗ 轉帳失敗：{e}")
        return False


# 主程式
conn = create_bank_database()

# 顯示初始餘額
cursor = conn.cursor()
print("【初始餘額】")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(f"{row[0]} ({row[1]}): {row[2]} 元")

# 成功的轉帳
print("\n【轉帳 3000 元】")
transfer_money(conn, 'A001', 'A002', 3000)

# 顯示轉帳後餘額
print("\n【轉帳後餘額】")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(f"{row[0]} ({row[1]}): {row[2]} 元")

# 失敗的轉帳（餘額不足）
print("\n【嘗試轉帳 20000 元】")
transfer_money(conn, 'A001', 'A002', 20000)

# 顯示最終餘額（應該不變）
print("\n【最終餘額】")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(f"{row[0]} ({row[1]}): {row[2]} 元")

conn.close()
```

**範例檔案：** `unit06_sql_database/example05_transaction.py`

### 練習題

#### 練習 1：建立資料庫

**任務：** 建立課程資料庫，包含課程名稱、授課老師、學分數、上課時間。

**要求：**

1. 建立 `courses.db` 資料庫
2. 建立 `courses` 資料表
3. 插入至少 5 筆課程資料
4. 查詢並顯示所有課程

**練習檔案：** `unit06_sql_database/exercise01_create_database.py`

#### 練習 2：查詢練習

**任務：** 使用 SQLite 進行各種查詢操作。

**要求：**

1. 建立產品資料表（產品名稱、分類、價格、庫存、上架日期）
2. 插入至少 10 筆測試資料
3. 實作查詢功能：
   - 查詢特定分類的產品
   - 查詢價格區間的產品
   - 按價格排序
   - 統計每個分類的產品數量
   - 計算平均價格
   - 找出庫存不足（< 10）的產品

**練習檔案：** `unit06_sql_database/exercise02_query_practice.py`

#### 練習 3：成績統計系統

**任務：** 建立學生成績管理系統，包含多個資料表和統計功能。

**要求：**

1. 建立三個資料表：students（學生）、subjects（科目）、scores（成績）
2. 實作功能：
   - 新增學生、科目、成績
   - 查詢學生的所有成績
   - 計算學生的平均成績
   - 統計科目的平均分數
   - 找出每個科目的最高分學生
   - 列出不及格（< 60）的成績記錄

**練習檔案：** `unit06_sql_database/exercise03_grade_statistics.py`

#### 練習 4：圖書館借閱系統

**任務：** 建立完整的圖書館借閱管理系統。

**要求：**

1. 建立資料表：books（書籍）、members（會員）、borrowings（借閱記錄）
2. 實作功能：
   - 書籍管理（新增、查詢、更新庫存）
   - 會員管理（新增、查詢）
   - 借書（檢查庫存、建立記錄、更新庫存）
   - 還書（更新記錄、恢復庫存）
   - 查詢會員的借閱記錄
   - 查詢逾期未還的書籍
   - 統計熱門書籍
3. 使用交易處理確保資料一致性

**練習檔案：** `unit06_sql_database/exercise04_library_system.py`

### 重點觀念整理

**Q：為什麼要用資料庫而不是 CSV 或 JSON？**
→ 當資料量大、需要複雜查詢（如統計、排序、多表關聯）時，資料庫效能遠勝檔案。

**Q：什麼是 PRIMARY KEY？**
→ 主鍵，用來唯一識別每一筆資料，不能重複、不能是 NULL。

**Q：什麼是 FOREIGN KEY？**
→ 外鍵，用來建立資料表之間的關聯，確保資料完整性。

**Q：為什麼要用 ? 當佔位符而不是字串拼接？**
→ 防止 SQL Injection 攻擊，確保安全性。

**Q：什麼時候需要用 Transaction？**
→ 當一個操作需要更新多筆資料，且必須「全部成功或全部失敗」時。

**Q：JOIN 有幾種類型？**
→ INNER JOIN（交集）、LEFT JOIN（左表全留）、RIGHT JOIN（右表全留）、FULL JOIN（聯集）。

**Q：GROUP BY 和 WHERE 的差別？**
→ WHERE 在分組前篩選，HAVING 在分組後篩選。

### 實務應用場景

1. **學校成績管理**：學生資料、科目資料、成績記錄，多表關聯查詢
2. **電商訂單系統**：商品、訂單、顧客資料，統計銷售額、熱門商品
3. **圖書館借閱**：書籍、會員、借閱記錄，逾期提醒、熱門書籍統計
4. **員工打卡系統**：員工資料、打卡記錄，計算工時、出缺勤統計
5. **庫存管理**：產品資料、進貨記錄、銷售記錄，庫存警示

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請給我 SQLite 資料庫操作的完整範例
- 請幫我設計學生成績資料表結構
- 請給我用 Python 執行 SQL 查詢的範例
- 請解釋 INNER JOIN 和 LEFT JOIN 的差別並給範例
- 請幫我實作交易處理的範例
- 請解釋 GROUP BY 和 HAVING 的用法
- 請給我多表 JOIN 的實務範例
- 請幫我檢查 SQL 查詢語法是否正確
- 請給我防止 SQL Injection 的最佳實踐
- 請幫我設計圖書館借閱系統的資料表結構

---

## 單元 7：非關聯式資料（JSON / TinyDB）

### 為什麼要學 NoSQL？

想像你在管理「筆記本 App」，每篇筆記的內容都不一樣：

- 有些筆記只有純文字
- 有些筆記有標籤、圖片連結
- 有些筆記有清單、待辦事項
- 結構很「彈性」，不固定

**如果用 SQL？**

- 需要事先定義欄位：標題、內容、標籤 1、標籤 2、標籤 3...
- 如果某篇筆記有 10 個標籤怎麼辦？欄位不夠用！
- 每次改資料結構都要「ALTER TABLE」，很麻煩

**如果用 NoSQL？**

- 每篇筆記就是一個「文件（document）」
- 想加什麼欄位就加，非常彈性
- 標籤用列表 `["Python", "學習", "筆記"]`，想加幾個就加幾個

**NoSQL 的特點：**

- ✅ **彈性結構**：每筆資料可以有不同的欄位
- ✅ **快速開發**：不需要事先設計複雜的資料表結構
- ✅ **適合階層資料**：可以直接存巢狀的 JSON 結構
- ❌ **不適合複雜關聯**：多表 JOIN 查詢不如 SQL 方便
- ❌ **不適合交易處理**：缺乏 SQL 的 ACID 特性

### 生活範例：手機記事本

**情境：**
你的手機記事本就是典型的 NoSQL 應用！

```python
# 每篇筆記都是一個「文件」
note1 = {
    "id": 1,
    "title": "今日待辦",
    "content": "買菜、寫作業、運動",
    "tags": ["TODO"],
    "created_at": "2024-01-15"
}

note2 = {
    "id": 2,
    "title": "Python 學習筆記",
    "content": "學會了 TinyDB 的用法",
    "tags": ["Python", "學習", "程式設計"],
    "created_at": "2024-01-16",
    "rating": 5  # 這篇多了「評分」欄位！
}

note3 = {
    "id": 3,
    "title": "會議記錄",
    "content": "下週一專案會議",
    "tags": ["工作", "會議"],
    "created_at": "2024-01-17",
    "attachments": ["file1.pdf", "file2.docx"]  # 這篇多了「附件」欄位！
}
```

**注意到了嗎？**

- 每篇筆記的欄位不完全一樣
- `note2` 有評分，其他沒有
- `note3` 有附件，其他沒有
- 這就是 NoSQL 的「彈性」！

### 什麼情況用 SQL / 什麼情況用 NoSQL?

#### 比較適合 SQL 的情境：

需要強一致性、交易（轉帳、下單）、多表關聯、複雜查詢（多條件、JOIN、子查詢）。

#### 比較適合 NoSQL 的情境：

需要超大量資料、超多使用者、資料結構常變、讀寫頻率很高但查詢邏輯相對簡單，例如：貼文牆、快取、session、log 搜集。

### 程式範例

#### 範例 1：使用 TinyDB 資料庫

TinyDB 是一個「用 JSON 檔當底層儲存的、輕量級 Python NoSQL 文件資料庫」，專門給小型專案用

**安裝 TinyDB：**

```bash
pip install tinydb
```

```python
from tinydb import TinyDB, Query


# 建立資料庫
db = TinyDB('library.json', indent=2, ensure_ascii=False)

# 新增書籍（Insert）
books = [
    {
        'title': 'Python 程式設計入門',
        'author': '王小明',
        'isbn': '978-1234567890',
        'quantity': 5,
        'category': '程式設計'
    },
    {
        'title': '資料科學基礎',
        'author': '李小華',
        'isbn': '978-2345678901',
        'quantity': 3,
        'category': '資料科學'
    },
    {
        'title': 'JavaScript 實戰',
        'author': '張大同',
        'isbn': '978-3456789012',
        'quantity': 7,
        'category': '程式設計'
    }
]

# 插入多筆資料
doc_ids = db.insert_multiple(books)
print(f"✓ 已新增 {len(doc_ids)} 本書籍")

# 查詢所有書籍（Read All）
all_books = db.all()
for book in all_books:
    print(f"{book['title']} ({book['author']})")

# 條件查詢（Read with Query）
Book = Query()

# 查詢分類為「程式設計」的書籍
results = db.search(Book.category == '程式設計')
print(f"\n程式設計類書籍共 {len(results)} 本")

# 查詢庫存大於 4 本的書籍
results = db.search(Book.quantity > 4)
for book in results:
    print(f"{book['title']}: {book['quantity']} 本")

# 更新資料（Update）
db.update({'quantity': 8}, Book.title == 'Python 程式設計入門')
print("✓ 已更新書籍庫存")

# 刪除資料（Delete）
db.remove(Book.isbn == '978-3456789012')
print("✓ 已刪除書籍")

# 關閉資料庫
db.close()
```

**範例檔案：** `unit07_nosql_data/example01_tinydb_basic.py`

#### 範例 2：TinyDB 進階查詢電影資料庫

```python
from tinydb import TinyDB, Query, where


# 建立電影資料庫
db = TinyDB('movies.json', indent=2, ensure_ascii=False)
db.truncate()

movies = [
    {
        'title': '肖申克的救贖',
        'director': '法蘭克·戴拉邦',
        'year': 1994,
        'genres': ['劇情', '犯罪'],
        'rating': 9.3,
        'box_office': 28.34
    },
    {
        'title': '星際效應',
        'director': '克里斯多福·諾蘭',
        'year': 2014,
        'genres': ['科幻', '劇情'],
        'rating': 8.6,
        'box_office': 677.47
    },
    {
        'title': '全面啟動',
        'director': '克里斯多福·諾蘭',
        'year': 2010,
        'genres': ['動作', '科幻', '驚悚'],
        'rating': 8.8,
        'box_office': 829.90
    }
]

db.insert_multiple(movies)

# 複雜查詢
Movie = Query()

# 1. 複雜邏輯查詢：評分 > 8.5 且票房 > 500M
print("【評分 > 8.5 且票房 > 500M 的電影】")
results = db.search((Movie.rating > 8.5) & (Movie.box_office > 500))
for movie in results:
    print(f"{movie['title']}: 評分 {movie['rating']}, 票房 ${movie['box_office']}M")

# 2. OR 查詢
print("\n【1990 年代或 2010 年代的電影】")
results = db.search(
    ((Movie.year >= 1990) & (Movie.year < 2000)) |
    ((Movie.year >= 2010) & (Movie.year < 2020))
)
for movie in results:
    print(f"{movie['title']} ({movie['year']})")

# 3. 列表包含查詢
print("\n【類型包含「科幻」的電影】")
results = db.search(Movie.genres.any(['科幻']))
for movie in results:
    print(f"{movie['title']}: {', '.join(movie['genres'])}")

# 4. 自訂查詢函數
print("\n【票房是評分 100 倍以上的電影】")
results = db.search(
    Movie.box_office.test(lambda val, movie: val > movie['rating'] * 100)
)
for movie in results:
    print(f"{movie['title']}")

# 5. 統計查詢
all_movies = db.all()
avg_rating = sum(m['rating'] for m in all_movies) / len(all_movies)
print(f"\n平均評分: {avg_rating:.2f}")

db.close()
```

**範例檔案：** `unit07_nosql_data/example02_tinydb_query.py`

### 練習題

#### 練習：使用 TinyDB 建立待辦事項

**任務：** 使用 TinyDB 建立待辦事項管理系統。

**要求：**

1. 實作 `TodoManager` 類別
2. 每個待辦事項包含：
   - 標題、描述、優先順序（高/中/低）
   - 狀態（待辦/進行中/已完成）
   - 建立時間、完成時間
3. 實作功能：
   - 新增待辦事項
   - 查詢待辦事項（依狀態、優先順序）
   - 更新狀態
   - 標記為完成
   - 刪除待辦事項

**練習檔案：** `unit07_nosql_data/exercise01_tinydb_todo.py`

### 常見問題

**Q：NoSQL 和 SQL 有什麼差別？**
→ SQL 是「關聯式」（表格結構、固定欄位），NoSQL 是「文件式」（彈性結構、類似 JSON）。

**Q：什麼時候用 NoSQL？什麼時候用 SQL？**
→ 用 NoSQL：資料結構彈性、快速開發、不需複雜關聯查詢。
→ 用 SQL：資料結構固定、需要複雜的多表 JOIN、需要交易處理（ACID）。

**Q：TinyDB 適合什麼場景？**
→ 小型專案、快速原型開發、不需要高效能的應用。不適合大量資料或高並發。

**Q：JSON 和 TinyDB 的差別？**
→ JSON 是「檔案格式」，需要自己寫程式讀寫；TinyDB 是「資料庫」，提供查詢、更新等功能。

**Q：為什麼 NoSQL 不適合複雜關聯？**
→ 因為沒有 JOIN 功能，如果要查詢「學生的所有課程成績」，需要寫程式手動關聯。

**Q：什麼是文件（Document）？**
→ 在 NoSQL 中，每一筆資料就是一個「文件」，類似 Python 的字典或 JSON 物件。

### 實務應用場景

1. **筆記 App**：每篇筆記結構不固定，適合 NoSQL
2. **使用者設定**：每個使用者的設定可能不同，用 JSON 儲存
3. **日誌記錄**：快速記錄各種事件，不需要事先定義欄位
4. **快速原型**：開發初期資料結構還不確定，用 NoSQL 快速迭代
5. **配置管理**：應用程式設定檔，用 JSON 或 TinyDB 管理

### SQL vs NoSQL 選擇指南

| 特性               | SQL（關聯式）      | NoSQL（文件式）    |
| ------------------ | ------------------ | ------------------ |
| **資料結構** | 固定欄位、表格式   | 彈性、類似 JSON    |
| **查詢能力** | 強大（JOIN、統計） | 基礎查詢           |
| **交易處理** | 支援 ACID          | 通常不支援         |
| **適合場景** | 複雜關聯、統計分析 | 快速開發、彈性結構 |
| **範例**     | 學生成績、訂單系統 | 筆記 App、設定檔   |

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請解釋 NoSQL 和關聯式資料庫的區別並給範例
- 請給我 TinyDB 的完整使用範例
- 請幫我實作一個簡單的記事本 app
- 請給我按日期和標籤分類的實作方法
- 請幫我為記事本 app 加上搜尋功能
- 請解釋什麼時候該用 SQL，什麼時候該用 NoSQL
- 請給我 TinyDB 複雜查詢的範例
- 請幫我設計適合 NoSQL 的資料結構
- 請給我使用 JSON 作為資料庫的最佳實踐
- 請比較 JSON、TinyDB、SQLite 的優缺點

---

## 期末整合專案：學生成績管理系統 v3

### 專案目標

整合學過的所有能力：

- OOP
- 模組化
- SQL 操作
- JSON 備份
- CSV 匯出
- 整理格式、輸入輸出

### 功能需求

- 科目的 CRUD（新增、讀取、更新、刪除）
- 學生資料的 CRUD
- 各科目成績排名
- 特定科目匯出成績

### 專案結構

- models.py（資料模型）
- database.py（資料庫操作）
- utils.py（工具函式）
- main.py（主程式入口）
