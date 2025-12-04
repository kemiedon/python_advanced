# AI 指令規範書

## 語言規定

- **必須使用繁體中文** 進行所有對話和文檔編寫

## 提交規範

- 每當完成一個任務後，自動 push 到 repository
- Commit 訊息按照以下格式命名：`日期-時間-版本[編號]`
  - 範例：`2025-11-22-17:20:46-1.0[建立專案結構]`
  - 日期格式：YYYY-MM-DD
  - 時間格式：HH:MM:SS（24 小時制）
  - 版本編號：1.0, 1.1, 1.2...（主版本.次版本，按照當日提交次數遞增）
  - 編號說明：用方括號括起來的簡要說明
- 每次 commit 說明需要整理該次更新的內容重點

## 指令歷史

### 第 1 個指令（Commit: a）

- 建立 SPEC 文件夾結構
- 建立 MAIN.md（專案規格書）和 PROMPT_GUIDE.md（AI 指令規範書）

### 第 2 個指令（Commit: b）

- 更新 PROMPT_GUIDE.md 加入語言規定和提交規範
- 第一次 commit 並 push

### 第 3 個指令（Commit: c）

- 調整待辦事項，移除文件更新相關項目，只保留教材編修相關部分
- 新建 python_advance.md 檔案作為主要教材內容
- 設定標題為「Python 進階課程」

### 第 4 個指令（Commit: d）

- 更新指令歷史記錄

### 第 5 個指令（Commit: f）

- 整理 Python 進階課程教材內容到 python_advance.md
- 按照規則進行整理：Markdown 格式、移除 emoji、統一副標題語意
- 每個單元加入生活化範例、程式範例、練習題、常見問題
- 每個單元加入 AI 協助學習 Prompt 區塊供學生複習
- 更新 MAIN.md 待辦事項，包含 8 個單元和期末專案

### 第 6 個指令（Commit: g）

- 更新單元 1：物件導向基礎（OOP）教材內容
- 加入「什麼是 OOP（物件導向程式設計）？」完整說明
- 加入物件導向的三個元素表格
- 加入偽代碼和真實 Python 程式範例
- 更新練習題為新的練習內容

### 第 7 個指令（Commit: 2025-11-22-17:XX:XX-1.2）

- 調整單元 1 的教材結構
- 將「什麼是 OOP」和「物件導向的三個元素」表格移至生活化範例上方
- 將原有生活化範例文字保留，放在「物件（Object）是類別（Class）的實例」下方

### 第 8 個指令（Commit: 2025-11-23-10:29:04-1.5）

- 在 `python_advanced/` 資料夾下建立 9 個單元的子資料夾（英文命名）
  - unit01_oop_basics, unit02_oop_advanced, unit03_modularity, unit04_builtin_modules
  - unit05_closure_decorator, unit06_file_data_processing, unit07_sql_database
  - unit08_nosql_data, final_project
- 為單元 1 新增程式範例與練習題解答
  - student_example1.py：Student 類別基礎實作
  - student_example2.py：使用多個物件和排序
  - exercise_solutions.py：練習題解答（Student 類別、WashingMachine 類別）
- 更新 SPEC/MAIN.md 加入資料夾結構規範及說明資料夾命名使用英文
- 標記單元 1 待辦事項為已完成

### 第 9 個指令（Commit: 2025-11-23-10:35:51-1.7）

- 用教材中 OOP 基本範例替換單元 1 程式檔案
- 刪除 student_example1.py、student_example2.py
- 新增 animal_example.py：Animal、Dog、Cat 類別展示繼承與多型

### 第 10 個指令（Commit: 2025-11-23-10:41:22-1.8）

- 統一所有單元的重點標題為「本單元重點」
- 每個單元補充完整的重點內容列表

### 第 11 個指令（Commit: 2025-11-23-10:42:08-1.9）

- 將「本單元重點」改為「單元重點」（全部 8 個單元）

### 第 12 個指令（Commit: 2025-11-23-11:18:56-2.0）

- 將單元 1 的練習題排版格式統一為單元 2 的格式
- 改為編號練習題（練習 1、練習 2）、難度標記（⭐、⭐⭐）
- 加入任務說明、期望輸出範例

### 第 13 個指令（Commit: 2025-11-23-XX:XX:XX-2.1）

- 為單元 2 建立程式範例與練習題解答
  - inheritance_example1.py：教材說明中的範例代碼（Student、ForeignStudent、多型示範）
  - exercise_solutions.py：包含練習 1-4 的完整解答（4 個練習題）
- 在 python_advanced/unit02_oop_advanced/ 資料夾中新增上述檔案
- 所有程式碼已測試並正確執行

### 第 14 個指令（Commit: 2025-11-23-11:25:00-2.2）

- 重命名 `unit03_modularity/` 中的原始檔案：`bread.py` -> `exercise01_bread.py`、`lettuce.py` -> `exercise02_lettuce.py`、`sandwich_main.py` -> `exercise03_sandwich.py`，並在各檔加入 docstring 與封裝函式。

### 第 15 個指令（Commit: 2025-11-23-11:27:12-2.3）

- 刪除 `unit03_modularity/` 的舊 wrapper 檔案（`bread.py`、`lettuce.py`、`sandwich_main.py`）以及對應的 `__pycache__/` 目錄，清理命名與快取衝突。

### 第 16 個指令（Commit: 2025-11-23-11:28:30-2.4）

- 在 `exercise03_sandwich.py` 新增匯入相容性處理（try/except）以同時支援 package relative 與 top-level imports，避免 ModuleNotFoundError。

### 第 17 個指令（Commit: 2025-11-23-11:30:05-2.5）

- 新增 `python_advanced/unit03_modularity/README.md`，說明三個 exercise 的用途、執行方式與範例輸出。

### 第 18 個指令（Commit: 2025-11-23-11:32:10-2.6）

- 建立 `python_advanced/unit04_builtin_modules/`，並新增範例與練習檔：`exercise01_random.py`、`exercise02_math.py`、`exercise03_datetime.py`、`exercise04_filesystem.py`、`save_students.py`、`load_students.py` 等。

### 第 19 個指令（Commit: 2025-11-23-11:34:20-2.7）

- 更新教材與總覽文件：修改 `python_advanced.md`、`python_advanced/MAIN.md` 與 `SPEC/MAIN.md`，同步新檔名、單元說明與完成狀態（將單元 2/3/4 標為已完成）。

### 第 20 個指令（Commit: 2025-11-23-11:36:45-2.8）

- 執行並驗證範例：在專案根目錄執行 `exercise03_sandwich.make_sandwich()`、`python3 python_advanced/unit04_builtin_modules/exercise01_random.py`、`python3 python_advanced/unit04_builtin_modules/exercise03_datetime.py` 等，確認輸出與行為正常。

### 第 21 個指令（Commit: 2025-11-23-11:38:00-2.9）

- 把上述操作摘要附加回 `SPEC/PROMPT_GUIDE.md` 的「指令歷史」區塊，並更新 TODO 列表以供追蹤（包含將操作列為已完成項目）。

### 單元 Commit 整理建議

為了讓 Git 歷史清晰、容易回溯，建議將操作按單元或類型分組成多個 commit（或用一個合併 commit）：

- **Unit 03（模組化）**：包含重命名檔案、相容性處理與 README，建議 commit 訊息：
  - `2025-11-23-11:25-2.2[unit03: rename and refactor exercises]`
- **Unit 04（內建模組）**：新增整個 unit 的範例與練習檔，建議 commit 訊息：
  - `2025-11-23-11:32-2.6[unit04: add builtin module examples and exercises]`
- **文件更新**：更新 `python_advanced.md`、`MAIN.md`、`SPEC/MAIN.md`，建議 commit 訊息：
  - `2025-11-23-11:34-2.7[docs: update unit filenames and status]`
- **執行驗證**：把驗證腳本的執行結果或測試檔（若有）一併 commit，建議 commit 訊息：
  - `2025-11-23-11:36-2.8[test: run examples and verify outputs]`
- **選項**：若希望保持單一乾淨 commit，可合併上述為一個合併 commit，例如：
  - `2025-11-23-11:40-2.9[feat: unit03-04 refactor, docs update, verify]`

以上為建議的 commit 拆分策略；如果你同意，我可以幫你執行 `git add` 與分別或合併的 `git commit`（請回覆要使用的策略：「分拆 commit」或「合併成一個 commit」）。
