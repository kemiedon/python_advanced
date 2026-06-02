"""practice_06_retry.py

【練習 06】裝飾器 — API 呼叫重試機制

情境：
  呼叫外部 API 時，偶爾會因為網路不穩而失敗。
  與其讓程式直接崩潰，可以用裝飾器自動重試幾次，
  等一下再試，直到成功或超過次數為止。

提示：
  - 在 wrapper 裡用 for 迴圈重試最多 MAX_RETRY 次
  - 用 try / except 捕捉例外
  - 失敗時用 time.sleep(1) 等待 1 秒再試
  - 成功就立刻 return，不再重試
  - 所有次數都失敗才印出「已達最大重試次數」
"""

import time
import random

MAX_RETRY = 3   # 最多重試次數


def retry(func):
    def wrapper(*args, **kwargs):
        for attempt in range(1, MAX_RETRY + 1):
            try:
                # TODO: 呼叫原始函式並回傳結果
                result = ___
                print(f"✅ 第 {attempt} 次成功")
                return result
            except Exception as e:
                print(f"❌ 第 {attempt} 次失敗：{e}")
                if attempt < MAX_RETRY:
                    print("   等待 1 秒後重試...")
                    # TODO: 等待 1 秒
                    ___
        print("🚫 已達最大重試次數，放棄。")
        return None

    return wrapper


# ── 模擬一個不穩定的 API ─────────────────────────────────────
@retry
def call_weather_api(city):
    """
    模擬呼叫天氣 API：有 60% 機率失敗（模擬網路不穩）
    """
    if random.random() < 0.6:
        raise ConnectionError("網路連線逾時")
    return f"{city} 今天晴天，28°C"


@retry
def call_stock_api(symbol):
    """
    模擬呼叫股價 API：有 70% 機率失敗
    """
    if random.random() < 0.7:
        raise TimeoutError("伺服器回應逾時")
    return f"{symbol} 目前股價：$150.25"


# ══════════════════════════════════════════════════════
#  主程式
# ══════════════════════════════════════════════════════
if __name__ == "__main__":
    random.seed(42)   # 固定隨機種子，讓結果可重現

    print("=== 查詢天氣 ===")
    result = call_weather_api("台北")
    if result:
        print(f"結果：{result}")

    print("\n=== 查詢股價 ===")
    result = call_stock_api("AAPL")
    if result:
        print(f"結果：{result}")
