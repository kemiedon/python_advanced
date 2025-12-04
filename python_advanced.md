# Python 進階課程

## 單元 1：物件導向基礎（OOP）

### 生活化範例

以下用更口語的方式說明，方便上課講解或當教材筆記：

- 閉包（Closure）怎麼想：

  - 想像有一本專屬的小筆記本，只屬於某一個函式。每次那個函式做事，就把資料寫進筆記本，筆記本會一直記得這些資料。即使原來那個寫筆記的程式不再執行，筆記本（閉包）會保存狀態。實務上常用來做「計數器」或「保存私人狀態」的工具。

- 裝飾器（Decorator）怎麼想：

  - 裝飾器就像在原本功能外面包一層附加程序，像門禁系統先檢查身份、或是幫函式加日誌、計時。你不需要改原來的函式，直接把裝飾器套上去就能在執行前後加事情。

上課示範建議：

- 閉包示範：

  - 實作一個簡單的計數器工廠（每個學生建立自己的 counter），讓學生各自呼叫自己的 counter，觀察數字各自遞增、互不干擾。
  - 實作 `@require_login` 模擬門禁：未登入的呼叫會被拒絕，已登入的才執行原本功能。
  - 再示範 `@timeit`，讓學生比較不同函式被裝飾前後的執行時間輸出，說明裝飾器可用來做性能監控。

而是「有一個桌子模板（Class）」，
你家有一張 IKEA 的桌子、朋友家也有一張，但都是那個模板做的（Object）。

Python 也一樣：

#### 物件導向的三個元素

| ---------------- | ---------------------------------------------- | ----------------------- |
| 物件（Object） | 具體存在、可操作的程式實體 | 通常指由類別產生的實例 |
| 類別（Class） | 定義一群物件的屬性與行為藍圖 | class 類別名稱: |
| 實例（Instance） | 根據類別建立的具體物件，每個實例可有不同屬性值 | 實例 = 類別名稱(參數) |

### 生活化範例

以下用簡單、口語的方式說明，並附上重點與範例，可直接在課堂演示。

專屬筆記本（閉包的比喻）

- 想像每位學生有一本只屬於他的筆記本，老師（外層函式）把筆記本交給學生後就離開，但筆記本會一直記下學生做過的事。無論過了多久，學生翻開筆記本，裡面的記錄都還在——這就是閉包的概念。

範例：

```python
def make_counter(name):
   count = 0  # 外層變數
   def add_one():
      nonlocal count
      count += 1
      print(f"{name} 的計數：{count}")
   return add_one

# 每位學生有自己的計數器
小明計數 = make_counter("小明")
小美計數 = make_counter("小美")

小明計數()  # 小明 的計數：1
小明計數()  # 小明 的計數：2
小美計數()  # 小美 的計數：1
小美計數()  # 小美 的計數：2

# 注意：小明的計數和小美的計數互不干擾！
```

重點：

- 每個閉包都有自己的「私人變數」，互不影響。
- 閉包常用於計數器、狀態儲存、以及工廠函式（返回特定行為的函式）。

門禁系統（裝飾器的比喻）

- 想像你來公司上班，門禁系統會先檢查你的識別證（前置動作），確認你有權限才放你進去做工作（真正的功能）。下班時，門禁系統記錄你離開的時間（後置動作）。門禁系統沒改變你「工作」這件事本身，只是在前後加了檢查與記錄，這就是裝飾器的用途。

範例 1：簡單的裝飾器（記錄執行時間）

```python
import time

def timeit(func):
   def wrapper():
      print(f"開始執行 {func.__name__}")
      start = time.time()
      func()
      end = time.time()
      print(f"執行時間：{end - start:.2f} 秒")
   return wrapper

@timeit
def slow_task():
   time.sleep(1)
   print("完成任務")

slow_task()
```

執行結果示例：

```
開始執行 slow_task
完成任務
執行時間：1.00 秒
```

範例 2：門禁裝飾器（檢查權限）

```python
def require_login(func):
   def wrapper(user):
      if not user:
         print("❌ 請先登入")
         return
      print("✓ 已驗證身份，開始執行")
      func(user)
   return wrapper

@require_login
def access_system(user):
   print(f"歡迎 {user}，進入系統")

access_system("小明")    # ✓ 已驗證身份，開始執行 / 歡迎 小明，進入系統
access_system(None)      # ❌ 請先登入
```

重點：

- 裝飾器可以在不改變原本函式的情況下，幫你加上「前置或後置」行為（例如權限檢查、執行時間紀錄、快取、錯誤處理、輸入驗證等）。

| 方法（Method） | 實例能執行的動作，定義在類別中 | def 方法名稱(self): |

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

**範例檔案：** `python_advanced/unit01_oop_basics/animal_example.py`

### 練習題

#### 練習 1：基礎類別設計（難度：⭐）

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

#### 練習 2：類別屬性設計（難度：⭐⭐）

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

**練習檔案：** `python_advanced/unit01_oop_basics/exercise01_student_grade.py`、`python_advanced/unit01_oop_basics/exercise02_washing_machine.py`

### 常見問題

**Q：self 是什麼？**
→ 就是「我自己」。物件在跟自己說話。

**Q：Class 一定要大寫？**
→ 不是規定，但習慣，大家都這樣寫。

**Q：物件跟變數差在哪？**
→ 物件有「資料 + 功能」。變數只有值。

#### 模組化實作練習：做三明治（難度：⭐⭐）

請依下列步驟完成一個「三明治製作」的模組化程式（已在示範檔中提供範例）：

1. 建立三個檔案（本教材檔案命名規範）：

   - `exercise01_bread.py`：實作 `cut_bread()`，負責切麵包並列印 `麵包切好了！`
   - `exercise02_lettuce.py`：實作 `prepare_lettuce()`，負責準備生菜並列印 `生菜洗好了！`
   - `exercise03_sandwich.py`：整合模組，匯入前兩個模組並實作 `make_sandwich()`，最後列印 `三明治完成！`

2. 在 `exercise03_sandwich.py` 中，請使用匯入語句（支援相對或頂層匯入）呼叫 `cut_bread()` 與 `prepare_lettuce()`。
3. `exercise03_sandwich.py` 應包含 `if __name__ == "__main__"`，以便可以直接執行作為腳本測試。
4. 將三個檔案放在 `unit03_modularity` 資料夾內，並以教材提供的檔名為準。

**注意：** 若其他程式仍以舊檔名引用，本教材保留相容性處理；但正式練習請以 `exercise0X_*.py` 命名。

---

### 子類別覆寫父類別方法（method overriding）

如果有外國學生，想要用英文自我介紹，可以設計一個子類別 ForeignStudent，覆寫 introduce() 方法：

```python
class ForeignStudent(Student):
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am in grade {self.grade}.")
```

- 原本所有學生都是用中文介紹，外國學生則改用英文。

---

### 多型 (Polymorphism)-設計可擴充的程式架構

多型（Polymorphism）是指：多個不同子類別可以用統一的方式被呼叫，程式不用管「具體是哪一種」，只要是同一個家族，就能順利執行相同的操作。

我們可以設計一個統一的「自我介紹」流程，任何類型學生都可以用同一方法呼叫：

```python
def show_introduction(student):
    student.introduce()

ming = Student("小明", 3)
john = ForeignStudent("John", 2)

show_introduction(ming)   # 大家好，我是3年級的小明。
show_introduction(john)   # Hello, my name is John. I am in grade 2.
```

- 無論新增什麼特殊學生類型，只需繼承自 Student 並定義 introduce() 方法即可自動適用。

---

父類別集中共用功能 → 子類別可依需要客製化 → 多型讓介面一致、擴充容易

### 練習題

#### 練習 1：基礎父類別設計（難度：⭐）

學校要管理學生資料，所有學生都有「姓名」和「學號」兩項基本資訊，以及「顯示基本資訊」的功能。

**任務：**

```
1. 建立一個名為 Student 的父類別
2. 屬性：name（姓名）、student_id（學號）
3. 方法：show_info()，能夠印出「我是 [姓名]，學號是 [學號]」
4. 建立兩個學生實例並呼叫 show_info() 方法
```

**期望輸出：**

```
我是小明，學號是 S001
我是小花，學號是 S002

```

#### 練習 2：子類別覆寫方法（難度：⭐⭐）

學校有不同科系的學生（例如資訊系、英文系），他們除了基本資訊外，還需要顯示自己的專長。

**任務：**

```
1. 建立父類別 Student（含 name、student_id）
2. 建立子類別 ComputerStudent（資訊系學生）
   - 新增屬性：programming_language（程式語言）
   - 覆寫 show_info() 方法：「我是 [姓名]，專長是 [程式語言]」
3. 建立子類別 EnglishStudent（英文系學生）
   - 新增屬性：language_level（英文程度）
   - 覆寫 show_info() 方法：「我是 [姓名]，英文程度是 [程度]」
4. 分別建立各科系學生實例並呼叫 show_info()

```

**期望輸出：**

```
我是小明，專長是 Python
我是小花，英文程度是 Advanced
```

#### 練習 3：多型應用（難度：⭐⭐⭐）

學校要開辦「學生成果分享會」，不同科系的學生用不同方式展示自己的成果。

**任務：**

```
1. 建立父類別 Student（含 name）
2. 建立子類別 ComputerStudent 和 EnglishStudent
3. 在各子類別中實現 demonstrate()（展示）方法：
   - ComputerStudent.demonstrate()：「[姓名]展示了一個 Python 程式」
   - EnglishStudent.demonstrate()：「[姓名]朗讀了一篇英文文章」
4. 建立一個函式 student_showcase(students_list)
   - 接收一個學生清單
   - 對每個學生呼叫 demonstrate() 方法（多型應用）
5. 建立包含不同科系學生的清單，呼叫 student_showcase()


```

**期望輸出：**

```
小明展示了一個 Python 程式
小花朗讀了一篇英文文章
大衛展示了一個 Java 程式
```

#### 練習 4： 綜合應用 - 課程管理系統（難度：⭐⭐⭐⭐）

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

**範例檔案：** `python_advanced/unit02_oop_advanced/inheritance_example1.py`

**練習檔案：** `python_advanced/unit02_oop_advanced/exercise01_basic_parent_class.py`、`python_advanced/unit02_oop_advanced/exercise02_method_overriding.py`、`python_advanced/unit02_oop_advanced/exercise03_polymorphism.py`、`python_advanced/unit02_oop_advanced/exercise04_course_management.py`

### 常見問題

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

## 單元 3：模組化（把程式拆乾淨）

### 單元重點

- 了解模組化的核心概念與重要性
- 學會如何將程式拆分成多個檔案（模組）
- 熟悉 import 與模組的使用方法
- 實作 `__name__ == "__main__"` 的應用
- 提升程式可維護性與團隊協作效率

#### 什麼是「模組化」？

用最簡單的說法：「模組化」就是把你的程式拆小塊，每一塊都只管自己這件事。像積木一樣，把功能整理在不同的檔案，讓程式變得好管理、好維護。

#### 為什麼要模組化？

- 程式寫多了，功能一堆，如果都塞在一個檔案，根本找不到要改的東西。
- 分成一塊一塊，你要改哪一部分，就去那一塊找，超省時間。
- 跟別人合作時，也不會互相打架，大家各做各的部分。

#### 生活化範例

你家所有東西都塞同一個大箱子 → 亂得要死。
模組化就是把東西分門別類。

假設你要做一個「學生選課」小程式：

把管理學生的功能放一個檔案：

```python
# student.py
class Student:
    pass
```

把管理課程的功能放一個檔案：

```python
# course.py
def enroll():
    pass
```

寫一個主程式（main.py）只負責整合和執行：

```python
# main.py
from student import Student
from course import enroll

# 主程式只負責整合功能
```

**模組化**不只讓程式管理清楚，讓做專案像堆積木一樣，想要加東西、改東西更加方便。

### 練習題

##### 模組化實作練習：做三明治（難度：⭐⭐）

請依下列步驟完成一個「三明治製作」的模組化程式（教材範例已改為 `exercise0X` 命名）：

1. 建立或使用以下檔案：

   - `exercise01_bread.py`：實作 `cut_bread()`（切麵包）
   - `exercise02_lettuce.py`：實作 `prepare_lettuce()`（準備生菜）
   - `exercise03_sandwich.py`：主程式，匯入並呼叫前兩者以組合三明治

2. 在 `exercise03_sandwich.py` 中示範如何呼叫上述函式並在最後印出 `三明治完成！`。
3. 包含 `if __name__ == "__main__"`，以便直接執行測試。

請將檔案放在 `unit03_modularity` 資料夾中，並以 `exercise0X` 命名方式提交練習。

**練習檔案：** `python_advanced/unit03_modularity/exercise01_bread.py`、`python_advanced/unit03_modularity/exercise02_lettuce.py`、`python_advanced/unit03_modularity/exercise03_sandwich.py`

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

## 單元 4：Python 內建模組

### 單元重點

- 學會看官方文件
- 操作常用模組：os、pathlib、datetime、shutil
- 檔案系統操作
- 時間和日期處理

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

2. random
   隨機數（抽籤、選號碼）

```python
import random
print(random.randint(1, 10))   # 隨機整數 1~10
print(random.choice(['A', 'B', 'C']))  # 隨機選一個
```

3. datetime
   處理時間與日期

```python
import datetime
now = datetime.datetime.now()
print(now)  # 現在時間
print(now.year, now.month, now.day)
```

4. os
   跟作業系統互動（像瀏覽檔案、建立資料夾）

```python
import os
print(os.listdir('.'))  # 列出目前資料夾的檔案
os.mkdir('testdir')     # 建立資料夾
```

5. sys
   取得 Python 系統與參數資訊

```python
import sys
print(sys.version)  # Python 版本
print(sys.argv)     # 執行程式時的參數清單
```

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

### 生活化範例

線上教學抽獎／隨機選人

需求：你要從一群學生名字裡，隨機抽出幸運兒、分組或作活動。

用到的模組：random

解法示範

```python
import random

students = ['小明', '小美', '阿強', '阿花', 'Amy', 'John']
winner = random.choice(students)
print(f"這次抽獎中獎學生是：{winner}")
```

延伸玩法：

如果要一次抽出三個人做小組

```python
group = random.sample(students, 3)
print("小組成員：", group)
```

如果要亂數排序所有名字分成兩組

```python
random.shuffle(students)
group1 = students[:3]
group2 = students[3:]
print("第一組：", group1)
print("第二組：", group2)
```

### 練習題

#### 練習 1：抽獎與分組（難度：⭐）

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

#### 練習 2：數學工具應用（難度：⭐）

使用 `math` 實作兩個小功能：

- `calc_hypotenuse(a, b)`：回傳直角三角形斜邊長（使用 `math.hypot` 或 sqrt）。
- `angle_to_radian_and_back(deg)`：將角度轉為弳度，計算 sin/cos 並回傳結果（使用 `math.radians`、`math.sin`、`math.cos`）。

期望示範：輸入 (3,4) 得到 5.0；輸入 90 度得到 sin≈1.0。

#### 練習 3：時間與檔名（難度：⭐）

使用 `datetime` 建立以時間為基礎的檔名與時間顯示：

- `timestamped_filename(prefix)`：回傳 `prefix_YYYYMMDD_HHMMSS.txt` 格式的檔名（使用 `datetime.now()` 與 `strftime`）。
- `print_now()`：印出目前年月日與時間的分別欄位（年/月/日/時/分/秒）。

範例輸出：

```
2025-11-23 14:30:05
filename: report_20251123_143005.txt
```

#### 練習 4：檔案系統基本操作（難度：⭐⭐）

使用 `os` 或 `pathlib` 實作簡單的檔案管理工具：

- `list_files(path)`：列出指定資料夾下所有檔案（使用 `os.listdir` 或 `pathlib.Path.iterdir()`）。
- `ensure_dir(path)`：如果資料夾不存在就建立（使用 `os.makedirs` 或 `Path.mkdir(parents=True, exist_ok=True)`)。
- `group_by_extension(path)`：把目錄下的檔案依副檔名分組並回傳字典（副檔名 -> 檔名清單）。

#### 練習 5：JSON 與系統參數（難度：⭐）

結合 `json` 與 `sys`：

- 寫一個程式 `save_students.py`，接受命令列參數（`sys.argv`）作為輸入檔名，將學生清單序列化為 JSON 存檔（使用 `json.dump`）。
- 寫一個對應的 `load_students.py`，讀取該 JSON 檔並列印資料。

範例：

```
save_students.py students.json load_students.py students.json
```

**範例檔案：** `python_advanced/unit04_builtin_modules/example_math.py`、`python_advanced/unit04_builtin_modules/example_random.py`、`python_advanced/unit04_builtin_modules/example_datetime.py`、`python_advanced/unit04_builtin_modules/example_os_pathlib.py`、`python_advanced/unit04_builtin_modules/example_json_sys.py`

**練習檔案：** `python_advanced/unit04_builtin_modules/exercise01_random.py`、`python_advanced/unit04_builtin_modules/exercise02_math.py`、`python_advanced/unit04_builtin_modules/exercise03_datetime.py`、`python_advanced/unit04_builtin_modules/exercise04_filesystem.py`、`python_advanced/unit04_builtin_modules/save_students.py`、`python_advanced/unit04_builtin_modules/load_students.py`

### AI 協助學習 Prompt

你可以使用以下 Prompt 來協助複習和練習：

- 請解釋 os、pathlib、datetime、shutil 的用途和區別
- 請給我一個自動分類檔案的完整範例
- 請幫我實作自動改檔名並加日期的功能
- 請幫我檢查檔案操作的程式碼是否正確

---

## 單元 5：閉包 & 裝飾器（@ 的真相）

### 單元重點

- 函式是可以被當成變數的
- 閉包 = 函式記得某個值
- 裝飾器可以替程式「加功能」
- 如何寫出可重複使用的裝飾器

### 什麼是閉包?（Closure）

- **定義**：閉包是一個函式，它能存取並記住外層函式的變數，就算外層函式已經執行結束。
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

- **定義**：裝飾器是一個函式，能在不改變原本功能的情況下，替其他函式增加額外的行為（前置或後置動作）。
- **範例**：

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

### 生活化範例

閉包（Closure）生活化比喻 — 計數器或專屬筆記本：

- 想像你有一個專屬的小筆記本（只屬於某個人），每次他做一件事就寫下一筆，筆記本會一直記得這個人的歷史記錄，即使你把寫下記錄的那個程式（外層函式）傳走或不再執行，筆記本（閉包）仍保有那個人的狀態（外層變數）。
- 在程式中，閉包常用來實作計數器、狀態儲存或工廠函式（返回特殊行為的函式）。

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

**範例檔案：** `python_advanced/unit05_closure_decorator/closure_example.py`

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

**範例檔案：** `python_advanced/unit05_closure_decorator/require_login_example.py`

裝飾器（Decorator）生活化比喻 — 門禁、日誌或前後處理：

- 例如你進公司要刷門禁，門禁系統會先檢查你有沒有權限（這是一層「前置」行為），通過才會到真正的辦公行為；這跟裝飾器很像，裝飾器在不改變原本功能的前提下，替函式增加前置或後置動作（例如權限檢查、記錄執行時間、錯誤處理、快取等）。
- 在實務上，裝飾器可用於輸入驗證、API 權限檢查、緩存或性能監控等情境。

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

**範例檔案：** `python_advanced/unit05_closure_decorator/timeit_example.py`（時間裝飾器範例）

### 練習題

練習 1：購物車的計數器（難度：⭐）

要求：

- 建立一個閉包函式儲存單一顧客的購物紀錄
- 支持「加商品」、「移除商品」、「查看購物車總額」三個操作
- 確保不同顧客的購物車互不影響

練習 2：銀行提款限制（難度：⭐⭐）

要求：

- 建立一個裝飾器檢查提款金額是否超過每日限額（$5000）
- 建立另一個裝飾器檢查帳戶餘額是否足夠
- 套用兩個裝飾器到提款函式上

練習 3：API 呼叫的重試機制（難度：⭐⭐）

要求：

- 建立一個裝飾器，函式執行出錯時自動重試（3 次）
- 每次重試前等待 1 秒
- 顯示重試次數與結果

練習 4：自訂快取裝飾器（難度：⭐⭐⭐）

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

## 單元 6：檔案與資料處理（CSV / JSON / Error）

### 單元重點

- 讀寫檔案（文字檔案操作）
- 匯入匯出 CSV（處理表格資料）
- JSON 序列化與反序列化（資料交換格式）
- try-except 處理錯誤（健壯的程式設計）
- 資料驗證與清理（資料品質管理）

### 什麼是檔案與資料處理？

在實際應用中，我們經常需要：

- **儲存資料**：將程式產生的資料永久保存
- **讀取資料**：載入先前儲存的資料繼續處理
- **交換資料**：與其他系統或程式分享資料
- **備份資料**：避免資料遺失

Python 提供了豐富的工具來處理各種格式的檔案和資料。

### 生活化範例

#### 導師整理成績的困擾

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

**重點：**

- `with open()` 會自動關閉檔案，不用擔心忘記關閉
- `encoding="utf-8"` 確保中文不會亂碼
- `"w"` 寫入、`"r"` 讀取、`"a"` 附加

**範例檔案：** `python_advanced/unit06_file_data_processing/example01_basic_file.py`

### CSV 檔案處理

CSV（Comma-Separated Values）就是用逗號分隔的表格資料，像 Excel 的簡化版。

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

**重點：**

- `csv.writer()` 用來寫入 CSV
- `csv.DictReader()` 可以用欄位名稱存取資料（像字典）
- `encoding="utf-8-sig"` 確保 Excel 可以正確開啟中文

**範例檔案：** `python_advanced/unit06_file_data_processing/example02_csv_operations.py`

### JSON 處理

JSON（JavaScript Object Notation）是網路上最常用的資料交換格式。

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

**重點：**

- `json.dumps()` / `json.loads()` 處理字串
- `json.dump()` / `json.load()` 處理檔案
- `ensure_ascii=False` 確保中文正常顯示
- `indent=2` 讓 JSON 更易讀

**範例檔案：** `python_advanced/unit06_file_data_processing/example03_json_operations.py`

### 錯誤處理（try-except）

在處理檔案時，很多事情可能出錯：檔案不存在、格式錯誤、權限不足等。

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

**重點：**

- `try-except` 捕捉錯誤，避免程式崩潰
- `FileNotFoundError`：檔案不存在
- `ValueError`：資料格式轉換錯誤
- `finally`：無論如何都會執行（用於清理資源）

**範例檔案：** `python_advanced/unit06_file_data_processing/example04_error_handling.py`

### 資料驗證與清理

處理真實資料時，經常會遇到「髒資料」：

- 缺漏值（空白、None）
- 格式錯誤（應該是數字卻是文字）
- 超出範圍（年齡 -5 歲、分數 150 分）

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

**範例檔案：** `python_advanced/unit06_file_data_processing/example05_data_cleaning.py`

### 練習題

#### 練習 1：讀寫文字檔案（難度：⭐）

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

**練習檔案：** `python_advanced/unit06_file_data_processing/exercise01_read_write.py`

#### 練習 2：處理 CSV 成績資料（難度：⭐⭐）

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

**練習檔案：** `python_advanced/unit06_file_data_processing/exercise02_csv_grade.py`

#### 練習 3：JSON 資料備份與還原（難度：⭐⭐）

建立資料備份系統：

- `create_student_data()`：產生學生資料
- `backup_to_json(data, filename)`：備份到 JSON
- `restore_from_json(filename)`：從 JSON 還原
- `search_student(data, name)`：搜尋學生資料

**應用情境：**

程式意外關閉或資料遺失時，可以從 JSON 備份檔快速還原。

**練習檔案：** `python_advanced/unit06_file_data_processing/exercise03_json_backup.py`

#### 練習 4：資料驗證與錯誤處理（難度：⭐⭐⭐）

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

**練習檔案：** `python_advanced/unit06_file_data_processing/exercise04_data_validation.py`

#### 練習 5：綜合應用 - 學生成績管理系統（難度：⭐⭐⭐⭐）

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

**練習檔案：** `python_advanced/unit06_file_data_processing/exercise05_integrated_system.py`

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

## 單元 7：關聯式資料庫（SQL + SQLite）

### 單元重點

本單元學習如何使用 SQLite 資料庫進行資料管理：

- **資料庫基礎概念**：理解關聯式資料庫、資料表、欄位、記錄的概念
- **SQLite 操作**：建立資料庫、建立資料表、插入/更新/刪除資料
- **SQL 查詢語法**：SELECT、WHERE、ORDER BY、GROUP BY、JOIN 等
- **Python 連接資料庫**：使用 sqlite3 模組進行資料庫操作
- **交易處理**：使用 BEGIN、COMMIT、ROLLBACK 確保資料一致性
- **進階查詢**：多表 JOIN、聚合函數、子查詢等

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

### 生活化範例：學生成績管理

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

**範例檔案：** `python_advanced/unit07_sql_database/example01_basic_sqlite.py`

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

**範例檔案：** `python_advanced/unit07_sql_database/example02_crud_operations.py`

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

**範例檔案：** `python_advanced/unit07_sql_database/example03_query_examples.py`

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

**範例檔案：** `python_advanced/unit07_sql_database/example04_join_tables.py`

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

**範例檔案：** `python_advanced/unit07_sql_database/example05_transaction.py`

### 練習題

#### 練習 1：建立資料庫 ⭐

**任務：** 建立課程資料庫，包含課程名稱、授課老師、學分數、上課時間。

**要求：**

1. 建立 `courses.db` 資料庫
2. 建立 `courses` 資料表
3. 插入至少 5 筆課程資料
4. 查詢並顯示所有課程

**練習檔案：** `python_advanced/unit07_sql_database/exercise01_create_database.py`

#### 練習 2：查詢練習 ⭐⭐

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

**練習檔案：** `python_advanced/unit07_sql_database/exercise02_query_practice.py`

#### 練習 3：成績統計系統 ⭐⭐⭐

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

**練習檔案：** `python_advanced/unit07_sql_database/exercise03_grade_statistics.py`

#### 練習 4：圖書館借閱系統 ⭐⭐⭐⭐

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

**練習檔案：** `python_advanced/unit07_sql_database/exercise04_library_system.py`

### 重點觀念整理

**Q：為什麼要用資料庫而不是 CSV 或 JSON？**
→ 當資料量大、需要複雜查詢（如統計、排序、多表關聯）時，資料庫效能遠勝檔案。

**Q：什麼是 PRIMARY KEY？**
→ 主鍵，用來唯一識別每一筆資料，不能重複、不能是 NULL。

**Q：什麼是 FOREIGN KEY？**
→ 外鍵，用來建立資料表之間的關聯，確保資料完整性。

**Q：為什麼要用 ? 佔位符而不是字串拼接？**
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

## 單元 8：非關聯式資料（JSON / TinyDB）

### 單元重點

本單元學習 NoSQL（非關聯式資料庫）的概念和應用：

- **NoSQL 思維**：理解文件式資料庫的特點和適用場景
- **JSON 資料操作**：使用 JSON 作為簡單資料庫，儲存和查詢資料
- **TinyDB 基礎**：輕量級 NoSQL 資料庫的使用
- **TinyDB 查詢**：使用 Query 物件進行複雜條件查詢
- **文件設計**：如何設計適合 NoSQL 的資料結構
- **NoSQL vs SQL**：理解何時選擇 NoSQL，何時選擇 SQL

### 為什麼要學 NoSQL？

**生活情境：**
想像你在管理「筆記本 App」，每篇筆記的內容都不一樣：

- 有些筆記只有純文字
- 有些筆記有標籤、圖片連結
- 有些筆記有清單、待辦事項
- 結構很「彈性」，不固定

**用 SQL？**

- 需要事先定義欄位：標題、內容、標籤 1、標籤 2、標籤 3...
- 如果某篇筆記有 10 個標籤怎麼辦？欄位不夠用！
- 每次改資料結構都要「ALTER TABLE」，很麻煩

**用 NoSQL？**

- 每篇筆記就是一個「文件（document）」
- 想加什麼欄位就加，非常彈性
- 標籤用列表 `["Python", "學習", "筆記"]`，想加幾個就加幾個

**NoSQL 的特點：**

- ✅ **彈性結構**：每筆資料可以有不同的欄位
- ✅ **快速開發**：不需要事先設計複雜的資料表結構
- ✅ **適合階層資料**：可以直接存巢狀的 JSON 結構
- ❌ **不適合複雜關聯**：多表 JOIN 查詢不如 SQL 方便
- ❌ **不適合交易處理**：缺乏 SQL 的 ACID 特性

### 生活化範例：手機記事本

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

### 程式範例

#### 範例 1：使用 JSON 作為簡單資料庫

**目標：** 學習如何使用 JSON 檔案來儲存和管理資料，實現類似資料庫的基本功能。

**情境：** 管理個人聯絡人資料。

```python
import json
import os
from datetime import datetime


class ContactManager:
    """聯絡人管理系統"""

    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """載入聯絡人資料"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_contacts(self):
        """儲存聯絡人資料"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=2)

    def add_contact(self, name, phone, email=''):
        """新增聯絡人"""
        contact = {
            'id': self.generate_id(),
            'name': name,
            'phone': phone,
            'email': email,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        self.contacts.append(contact)
        self.save_contacts()
        print(f"✓ 已新增聯絡人：{name}")

    def generate_id(self):
        """生成唯一 ID"""
        if not self.contacts:
            return 1
        return max(c['id'] for c in self.contacts) + 1

    def find_by_name(self, name):
        """依姓名查詢聯絡人"""
        results = [c for c in self.contacts if name.lower() in c['name'].lower()]
        return results

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        """更新聯絡人資料"""
        contact = self.find_by_id(contact_id)

        if not contact:
            print(f"✗ 找不到 ID 為 {contact_id} 的聯絡人")
            return False

        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email is not None:
            contact['email'] = email

        self.save_contacts()
        print(f"✓ 已更新聯絡人 ID {contact_id}")

    def delete_contact(self, contact_id):
        """刪除聯絡人"""
        contact = self.find_by_id(contact_id)

        if not contact:
            print(f"✗ 找不到 ID 為 {contact_id} 的聯絡人")
            return False

        self.contacts.remove(contact)
        self.save_contacts()
        print(f"✓ 已刪除聯絡人：{contact['name']}")


# 使用範例
manager = ContactManager()
manager.add_contact("王小明", "0912-345-678", "ming@example.com")
manager.add_contact("李小華", "0923-456-789", "hua@example.com")

# 查詢
results = manager.find_by_name("小")
for contact in results:
    print(f"{contact['name']}: {contact['phone']}")

# 更新
manager.update_contact(1, phone="0911-111-111")

# 刪除
manager.delete_contact(2)
```

**範例檔案：** `python_advanced/unit08_nosql_data/example01_json_database.py`

#### 範例 2：TinyDB 基本操作

**目標：** 介紹 TinyDB 這個輕量級的 NoSQL 資料庫，學習基本的 CRUD 操作。

**情境：** 管理圖書館的藏書資料。

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

**範例檔案：** `python_advanced/unit08_nosql_data/example02_tinydb_basic.py`

#### 範例 3：TinyDB 進階查詢

**目標：** 學習 TinyDB 的進階查詢功能，包含複雜條件、自訂函數等。

**情境：** 管理電影資料庫，進行各種複雜查詢。

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

**範例檔案：** `python_advanced/unit08_nosql_data/example03_tinydb_query.py`

### 練習題

#### 練習 1：JSON 筆記本 ⭐⭐

**任務：** 使用 JSON 建立一個簡單的筆記本系統。

**要求：**

1. 實作 `NotesManager` 類別
2. 支援新增、查詢、更新、刪除筆記
3. 每則筆記包含：標題、內容、標籤、建立時間、更新時間
4. 支援依標籤篩選筆記
5. 資料存入 `notes.json` 檔案

**練習檔案：** `python_advanced/unit08_nosql_data/exercise01_json_notes.py`

#### 練習 2：TinyDB 待辦事項 ⭐⭐⭐

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

**練習檔案：** `python_advanced/unit08_nosql_data/exercise02_tinydb_todo.py`

### 重點觀念整理

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

| 特性         | SQL（關聯式）      | NoSQL（文件式）    |
| ------------ | ------------------ | ------------------ |
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
