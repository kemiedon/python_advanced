# Python 進階課程教材

本 repository 包含 Python 進階課程的完整教材與範例程式。

## 📚 課程內容

### 單元一：物件導向基礎（OOP）

- 類別與物件的概念
- 建構子與方法
- 封裝、繼承、多型

### 單元二：物件導向進階

- 繼承與方法覆寫
- 多型應用
- super() 的使用

### 單元三：模組化

- 模組的建立與匯入
- 套件結構
- `__init__.py` 的使用

### 單元四：內建模組

- random：隨機數生成
- math：數學運算
- datetime：日期時間處理
- os/pathlib：檔案系統操作
- json：JSON 資料處理
- sys：系統參數與命令列參數

### 單元五：閉包與裝飾器

- 閉包（Closure）的概念
- 裝飾器（Decorator）的使用
- 實務應用：登入驗證、計時器

### 單元六：檔案與資料處理

- 基本檔案讀寫
- CSV 檔案操作
- JSON 檔案處理
- 錯誤處理
- 資料清理與驗證

### 單元七：關聯式資料庫（SQL + SQLite）

- SQLite 基本操作
- CRUD 操作
- SQL 查詢語法
- 多表 JOIN
- 交易處理

### 單元八：非關聯式資料（JSON / TinyDB）

- JSON 資料庫
- TinyDB 基本操作
- TinyDB 進階查詢
- NoSQL vs SQL

### 期末專案

- 學生成績管理系統 v3
- 整合所有單元知識

## 📂 資料夾結構

```
python_advanced/
├── README.md                    # 本檔案
├── python_advanced.md          # 完整教材文件
├── SPEC/
│   └── PROMPT_GUIDE.md        # AI 指令規範
├── unit01_oop_basics/         # 單元一：OOP 基礎
├── unit02_oop_advanced/       # 單元二：OOP 進階
├── unit03_modularity/         # 單元三：模組化
├── unit04_builtin_modules/    # 單元四：內建模組
├── unit05_closure_decorator/  # 單元五：閉包與裝飾器
├── unit06_file_data_processing/ # 單元六：檔案處理
├── unit07_sql_database/       # 單元七：SQL 資料庫
├── unit08_nosql_data/         # 單元八：NoSQL 資料
└── final_project/             # 期末專案

```

## 🚀 使用方式

### 環境需求

- Python 3.12+
- 建議使用虛擬環境

### 安裝套件

```bash
pip install tinydb
```

### 執行範例

```bash
# 在專案根目錄執行
python unit01_oop_basics/animal_example.py
python unit04_builtin_modules/example_random.py
python unit07_sql_database/example01_basic_sqlite.py
```

## 📖 學習建議

1. **循序漸進**：按照單元順序學習，每個單元都建立在前面的基礎上
2. **動手實作**：每個單元都有練習題，務必親自完成
3. **理解概念**：不要只是背程式碼，要理解背後的概念
4. **AI 輔助**：善用教材中的「AI 協助學習 Prompt」區塊

## 📝 教材特色

- ✅ **生活化範例**：每個概念都用生活情境說明
- ✅ **完整程式碼**：所有範例都可直接執行
- ✅ **循序漸進**：從基礎到進階，難度逐步提升
- ✅ **實務導向**：練習題都是實際應用場景
- ✅ **AI 協助**：每單元提供 AI 學習 Prompt

## 👨‍💻 作者

廣瞻互動媒體設計 林靜君(Kemie)老師

## 📅 更新日期

2025-12-04
