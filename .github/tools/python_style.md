# Python 撰寫風格指引（依 auto_push 腳本的實際寫法抽象化，移除情境專屬資訊）

## 1. 檔頭與語系
- 檔案開頭使用 shebang（如需執行），後接簡潔 docstring 說明目的。
- 對使用者的輸出與註解採繁體中文；程式名稱與 API 維持英文。

## 2. 匯入與常數
- 標準庫匯入集中於檔案頂部；僅在需要時做函式內的延遲匯入。
- 共用設定（如預設編碼）統一以全域常數管理。

## 3. 函式分層與責任
- 把外部指令呼叫、訊息生成、流程控制拆成小函式，避免重複碼。
- 核心入口 `main()` 保持薄層：檢查環境 → 執行主要流程 → 結束。
- 需要暫時切換工作目錄時，務必記錄原目錄並在 finally 中復原。

## 4. 命令執行與錯誤處理
- 封裝外部命令呼叫（例如以 `subprocess.run`）並統一編碼/錯誤處理。
- 以印出「執行 / 成功 ✓ / 失敗 ✗」的模式回報狀態，訊息保持簡短。
- 捕捉 `subprocess.CalledProcessError`，輸出 stderr 摘要；嚴重時直接退出。

## 5. 流程風格
- 偏程序式腳本，不強制類別與型別註解；重視直觀可讀。
- 以同步、線性步驟為主，避免過度抽象與巢狀控制流。
- 使用清楚的步驟提示取代正式 logging，適合批次/自動化腳本。

## 6. 輸出與國際化
- 統一對使用者的訊息風格：開頭描述、成功勾勾、失敗叉叉，便於閱讀。
- 維持簡潔用語並避免專案特定名詞，讓腳本可重用於不同情境。

## 7. 安全與清潔度
- 在流程前先做必要的環境檢查（如是否位於合法工作區）。
- 遇到無事可做的情境要明確提示並結束，避免留下未預期狀態。
- 盡量讓每個步驟可獨立失敗且能被清楚辨識。

## 8. 簡化範例片段
```python
def run_command(command, description):
  try:
    print(f"執行: {description}...")
    subprocess.run(
      command,
      check=True,
      capture_output=True,
      text=True,
      encoding=DEFAULT_ENCODING,
      errors="replace",
    )
    print(f"✓ {description} 完成")
    return True
  except subprocess.CalledProcessError as e:
    stderr = (e.stderr or '').strip()
    print(f"✗ {description} 失敗: {stderr}")
    return False
```
