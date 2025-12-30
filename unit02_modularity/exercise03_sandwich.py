"""
練習 03-03 — 模組化整合 (make sandwich)

說明:
建立 `make_sandwich()` 函式，從 `exercise01_bread` 與 `exercise02_lettuce`
匯入所需函式並呼叫它們，最後印出 `三明治完成！`。

要求:
 - 使用 `from exercise01_bread import cut_bread`
 - 使用 `from exercise02_lettuce import prepare_lettuce`
 - 在模組被直接執行時（`if __name__ == "__main__"`）呼叫 `make_sandwich()`，
   以便可作為腳本執行測試。
"""

try:
    # 當作 package 匯入時使用相對路徑
    from .exercise01_bread import cut_bread
    from .exercise02_lettuce import prepare_lettuce
except Exception:
    # 直接以檔案執行或在非 package 狀態下，使用頂層匯入
    from exercise01_bread import cut_bread
    from exercise02_lettuce import prepare_lettuce


def make_sandwich():
    cut_bread()
    prepare_lettuce()
    print("三明治完成！")


if __name__ == "__main__":
    make_sandwich()
