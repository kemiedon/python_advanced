---
name: 教學文檔與範例程式碼編寫
description: 編寫符合規範的 Python 教學文檔與範例程式碼
---

# 工作流程

1. 確認「語言與格式」
2. 撰寫「範例程式碼」
3. 標示「檔案路徑」
4. 組織「檔案結構」
5. 驗證「規範遵守」

# STEP 1: 確認語言與格式要求
function 確認「語言與格式」:
  - 工具: read/readFile
  - 檢查是否使用繁體中文
  - 確認符合教學用詞與表達方式
  - 保持技術術語精準性

# STEP 2: 撰寫符合規範的範例程式碼
function 撰寫「範例程式碼」:
  - 工具: edit/createFile, edit/applyPatch
  - 根據教學目標建立範例程式碼
  - 加上清楚的註解說明
  - 確保程式碼簡潔易懂
  - 使用國中生能理解的詞彙與概念

# STEP 3: 標示所有檔案路徑
function 標示「檔案路徑」:
  - 工具: edit/applyPatch
  - 在範例程式碼區塊下方加上檔案路徑標示
    * 範例檔格式：`<font style='color: brown;'>範例檔參考: [相對路徑]</font>`
    * 練習檔格式：`<font style='color: darkblue;'>練習檔參考: [相對路徑]</font>`
    * 作業檔格式：`<font style='color: darkblue;'>作業檔參考: [相對路徑]</font>`
  - 確保路徑正確無誤

# STEP 4: 組織檔案到正確結構
function 組織「檔案結構」:
  - 工具: edit/createDirectory, edit/createFile
  - 將範例檔案與示範程式統一放到 examples/ 目錄
    * 依照章節編號分類
    * 同章節有多個範例時使用子編號（如 02-1, 02-2）
  - 將練習檔案放到 practice/ 目錄
  - 將作業檔案放到 homework/ 目錄

# STEP 5: 驗證是否符合所有規範
function 驗證「規範遵守」:
  - 工具: read/readFile, search/textSearch
  - 檢查是否使用繁體中文
  - 檢查檔案路徑標示格式是否正確
  - 檢查檔案是否放在正確的目錄
  - 檢查程式碼是否有清楚註解
  - 找出不符合規範的部分並修正

---

# 檔案組織規則

| 目錄      | 用途                       | 檔案命名規則                                      |
| --------- | -------------------------- | ------------------------------------------------- |
| examples/ | 教學範例程式碼與示範程式   | 章節編號_主題.py 或 章節編號-子編號_主題.py       |
| practice/ | 課堂練習題                 | 主題_exercise.py                                  |
| homework/ | 回家作業                   | exercise_編號_主題.py                             |

**範例命名說明：**
- 單一範例：`02_variables.py`
- 多個範例：`02-1_variables.py`, `02-2_naming.py`

---

# 檔案路徑標示格式
2-1_variables.py</font>`     
| 類型     | 顏色      | 格式範例                                                                           |
| -------- | --------- | ---------------------------------------------------------------------------------- |
| 範例檔   | brown     | `<font style='color: brown;'>範例檔參考: examples/01_variables_naming.py</font>`   |
| 練習檔   | darkblue  | `<font style='color: darkblue;'>練習檔參考: practice/cost_exercise.py</font>`      |
| 作業檔   | darkblue  | `<font style='color: darkblue;'>作業檔參考: homework/</font>`                      |
