# Unit07：關聯式資料庫（SQL + SQLite）範例與練習

本資料夾包含單元 7 中的範例與練習程式，示範 SQLite 資料庫操作、SQL 查詢、資料表設計等功能。

## 範例檔案

- `example01_basic_sqlite.py`：基本 SQLite 資料庫操作
- `example02_crud_operations.py`：增刪改查（CRUD）完整操作
- `example03_query_examples.py`：各種 SQL 查詢範例
- `example04_join_tables.py`：多表關聯查詢
- `example05_transaction.py`：交易處理與錯誤回復

## 練習檔案

- `exercise01_create_database.py`：練習 1 - 建立學生資料庫
- `exercise02_query_practice.py`：練習 2 - SQL 查詢練習
- `exercise03_grade_statistics.py`：練習 3 - 成績統計系統
- `exercise04_library_system.py`：練習 4 - 圖書館管理系統

## 執行範例（在專案根目錄）

```bash
# 範例檔案
python3 python_advanced/unit07_sql_database/example01_basic_sqlite.py
python3 python_advanced/unit07_sql_database/example02_crud_operations.py
python3 python_advanced/unit07_sql_database/example03_query_examples.py
python3 python_advanced/unit07_sql_database/example04_join_tables.py
python3 python_advanced/unit07_sql_database/example05_transaction.py

# 練習檔案
python3 python_advanced/unit07_sql_database/exercise01_create_database.py
python3 python_advanced/unit07_sql_database/exercise02_query_practice.py
python3 python_advanced/unit07_sql_database/exercise03_grade_statistics.py
python3 python_advanced/unit07_sql_database/exercise04_library_system.py
```

## 資料庫檔案

範例會自動產生所需的 SQLite 資料庫檔案：

- `students.db`：學生資料庫
- `library.db`：圖書館系統資料庫
- `practice.db`：練習用資料庫
