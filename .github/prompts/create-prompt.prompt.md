---
name: create_prompt
description: 用繁體中文、淺顯易懂、保留技術術語與精準度、Copilot 友善，建立含中繼資料與結構化步驟的提示檔
---

# 工作流程

1. 撰寫「中繼資料」
2. 撰寫「主要說明與流程」
3. 撰寫「函式定義」
4. 格式化「表格」
5. 驗證「格式規則」

# STEP 1: 在頂部撰寫中繼資料
function 撰寫「中繼資料」:
  - 工具: edit/createFile, edit/applyPatch
  - 在頂部新增中繼資料：name、description
  - 下方緊接「工作流程」區段（中間不留空行）

# STEP 2: 撰寫主要說明與流程
function 撰寫「主要說明與流程」:
  - 工具: edit/applyPatch
  - 使用中繼資料中的 description（簡短、清楚）
  - 加上「# 工作流程」標題
  - 中繼資料與工作流程之間需空一行
  - 建立提示檔時，函式名稱務必使用中文
  - 加入「語言與風格規定」：
    * 使用繁體中文
    * 用淺顯易懂的句子與詞彙（保持簡單）
    * 保留技術術語與技術精準度（名詞與介面名稱照用）
    * Copilot 友善：指令要簡短、直接、可操作（行動動詞開頭）
  - 依序列出函式呼叫（1. 撰寫「函式一」，2. 撰寫「函式二」...）
  - 使用簡短、容易懂的動作句（像偽代碼），保持清楚

# STEP 3: 撰寫函式定義
function 撰寫「函式定義」:
  - 工具: edit/applyPatch
  - 在每個 function 上方新增「# STEP n: 註解」
  - 使用 "function 動詞「主要名詞」:" 語法
  - 第一個條列項必為「工具: 類別/工具名（, 類別/工具名...）」
  - 工具列規則：
    * 可列多個工具，使用逗號分隔或分行
    * 每個工具必須在「可用工具」表內，格式為「類別/工具名」（例：edit/applyPatch）
    * 不得填「無」，至少列出一個具體工具
  - 以條列項列出步驟（-），句子簡短直接
  - 每句以動作動詞開頭，避免冗長

# STEP 4: 格式化表格
function 格式化「表格」:
  - 工具: edit/applyPatch
  - 對齊表格欄位，讓垂直分隔線整齊
  - 方法簽名若已含參數（直接寫在簽名中），就不要再在表格中加「參數」欄，避免重複

# STEP 5: 驗證格式規則
function 驗證「格式規則」:
  - 工具: read/readFile, search/textSearch, edit/applyPatch
  - 檢查頂部是否包含 name, description 與 --- 分隔線
  - 檢查是否包含「# 工作流程」標題及其下方的序號列表
  - 檢查序號列表中的函式名稱是否與下方的 function 名稱完全一致
  - 檢查每個步驟是否有 # STEP n: 註解與對應的 function 語句
  - 檢查是否所有函式名稱均為「動詞 + 主要名詞」並含「」標註（例如：撰寫「中繼資料」）
  - 檢查每個 function 的第一條項目是否為 工具 標記
  - 檢查每個 工具 標記所列的每一個工具皆在下方「可用工具」表內，且以「類別/工具名」格式填寫；不得為「無」
  - 允許列出多個工具，以逗號分隔或分行皆可；但至少需列出一個具體工具
  - 檢查語言與風格是否符合規定：使用繁體中文；句子簡單、淺顯易懂；保留技術術語與精準度；指令簡短、直接、可操作
  - 檢查巢狀清單符號是否符合規定：第一層使用 `-`，第二層使用 `*`，第三層使用 `+`
  - 檢查步驟函式區塊之間（即 function 之間）是否確實空了一行
  - 檢查 function 區塊內部的條列項目之間是否「沒有」額外空行
  - 確保所有指令簡潔直接，且使用淺顯易懂的詞彙但保留精確術語
  - 找到任何不符合上述結構或規則的部分並完成修復
  - 若檢查發現問題，使用 edit/applyPatch 進行修正

# 輸出範本

```
---
name: {prompt_name}
description: {用途描述}
---

# 工作流程

1. 定義「函式一」
2. 定義「函式二」
3. 格式化「表格」
4. 驗證「格式規則」

# STEP 1: 定義每個函式的用途
function 定義「函式一」:
  - 工具: edit/applyPatch, read/readFile
  - 步驟 1
    * 第二層示例（使用 * 作為符號）
      + 第三層示例（使用 + 作為符號）
  - 步驟 2
```

---

# 可用工具

| 編號 | 類別   | 工具                    | 參考                         | 說明                                       |
| ---- | ------ | ----------------------- | ---------------------------- | ------------------------------------------ |
| 1    | agent  | runSubagent             | agent/runSubagent            | 在隔離的次代理情境中執行任務，以利組織與委派 |
| 2    | edit   | createDirectory         | edit/createDirectory         | 在工作區建立新目錄                         |
| 3    | edit   | createFile              | edit/createFile              | 建立新檔案                                 |
| 4    | edit   | createJupyterNotebook   | edit/createJupyterNotebook   | 建立新的 Jupyter Notebook                  |
| 5    | edit   | applyPatch              | edit/applyPatch              | 編輯工作區中的檔案（套用 diff/patch）      |
| 6    | edit   | editNotebook            | edit/editNotebook            | 編輯工作區中的 Notebook 檔案               |
| 7    | execute| createAndRunTask        | execute/createAndRunTask     | 在工作區建立並執行任務                     |
| 8    | execute| getTerminalOutput       | execute/getTerminalOutput    | 取得先前啟動之終端機命令的輸出             |
| 9    | execute| runInTerminal           | execute/runInTerminal        | 在終端機執行指令                           |
| 10   | execute| runNotebookCell         | execute/runNotebookCell      | 觸發 Notebook 檔案中某個儲存格的執行        |
| 11   | execute| runTask                 | execute/runTask              | 執行工作區中的任務                         |
| 12   | execute| runTests                | execute/runTests             | 執行單元測試（可含覆蓋率）                 |
| 13   | execute| testFailure             | execute/testFailure          | 附上最近一次單元測試失敗的資訊             |
| 14   | read   | getNotebookSummary      | read/getNotebookSummary      | 取得 Notebook 儲存格列表與中繼資料         |
| 15   | read   | getTaskOutput           | read/getTaskOutput           | 取得任務輸出                               |
| 16   | read   | problems                | read/problems                | 檢查特定檔案的錯誤                         |
| 17   | read   | readFile                | read/readFile                | 讀取檔案內容                               |
| 18   | read   | readNotebookCellOutput  | read/readNotebookCellOutput  | 讀取 Notebook 儲存格最近一次執行的輸出      |
| 19   | read   | terminalLastCommand     | read/terminalLastCommand     | 取得目前終端的上一個指令                   |
| 20   | read   | terminalSelection       | read/terminalSelection       | 取得目前終端的選取內容                     |
| 21   | search | changes                 | search/changes               | 取得已變更檔案的差異                       |
| 22   | search | codebase                | search/codebase              | 在程式碼庫中尋找相關片段、符號與資訊       |
| 23   | search | fileSearch              | search/fileSearch            | 以 glob 模式依檔名搜尋                     |
| 24   | search | listDirectory           | search/listDirectory         | 列出目錄內容                               |
| 25   | search | searchResults           | search/searchResults         | 取得搜尋檢視的結果                         |
| 26   | search | textSearch              | search/textSearch            | 以正則表達式搜尋檔案文字                   |
| 27   | search | usage                   | search/usage                 | 列出函式、類別、方法或變數的所有使用位置   |
| 28   | todo   | todo                    | todo/todo                    | 管理與追蹤任務規劃的待辦項目               |
| 29   | vscode | extensions              | vscode/extensions            | 搜尋 VS Code 擴充功能                      |
| 30   | vscode | getProjectSetupInfo     | vscode/getProjectSetupInfo   | 取得工作區的專案設定資訊                   |
| 31   | vscode | installExtension        | vscode/installExtension      | 在 VS Code 安裝擴充功能                    |
| 32   | vscode | newWorkspace            | vscode/newWorkspace          | 在 VS Code 腳手架建立新的工作區            |
| 33   | vscode | openSimpleBrowser       | vscode/openSimpleBrowser     | 在簡易瀏覽器預覽本機網站                   |
| 34   | vscode | runCommand              | vscode/runCommand            | 在 VS Code 執行指令                         |
| 35   | vscode | vscodeAPI               | vscode/vscodeAPI             | 查閱 VS Code API 參考與文件以進行擴充開發   |
| 36   | web    | fetch                   | web/fetch                    | 擷取網頁主要內容                           |
| 37   | web    | githubRepo              | web/githubRepo               | 搜尋 GitHub 儲存庫中的相關原始碼片段        |
