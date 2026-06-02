"""practice_07_cache.py

【練習 07】帶參數的裝飾器 — 自訂快取

情境：
  計算某些結果很耗時（例如呼叫 API、複雜運算），
  同樣的輸入短時間內呼叫多次時，
  直接回傳上次的結果就好，不用重新算。
  用 @cache(timeout=30) 控制快取有效秒數。

提示：
  - 這是帶參數的裝飾器，結構為三層函式
  - 用 dict 存快取：{ 參數 : (結果, 存入時間) }
  - 用 time.time() 取得目前時間（秒）
  - 判斷快取是否過期：目前時間 - 存入時間 > timeout

三層結構：
  def cache(timeout):          ← 第一層：接收 timeout
      def decorator(func):     ← 第二層：接收函式
          def wrapper(*args):  ← 第三層：查快取 / 計算
              ...
          return wrapper
      return decorator
"""

import time


def cache(timeout=30):
    """
    帶參數的快取裝飾器。
    timeout: 快取有效時間（秒），預設 30 秒
    """
    def decorator(func):
        # 每個被裝飾的函式都有自己獨立的快取 dict
        # 格式：{ args : (result, timestamp) }
        _cache = {}

        def wrapper(*args):
            now = time.time()

            # TODO: 檢查 args 是否在 _cache 裡，且快取未過期
            #       過期條件：now - timestamp > timeout
            if args in _cache:
                result, timestamp = _cache[args]
                if ___:
                    print(f"[快取命中] {func.__name__}{args} → {result}")
                    return result
                else:
                    print(f"[快取過期] {func.__name__}{args}，重新計算...")

            # TODO: 快取沒有或已過期，呼叫原始函式計算結果
            result = ___

            # TODO: 把結果與目前時間存入 _cache
            _cache[args] = ___

            print(f"[重新計算] {func.__name__}{args} → {result}")
            return result

        return wrapper
    return decorator


# ══════════════════════════════════════════════════════
#  套用快取裝飾器
# ══════════════════════════════════════════════════════

@cache(timeout=3)   # 快取有效 3 秒（方便測試）
def get_exchange_rate(currency):
    """模擬查詢匯率（耗時操作）"""
    time.sleep(0.5)  # 模擬 API 延遲
    rates = {"USD": 32.5, "JPY": 0.22, "EUR": 35.8}
    return rates.get(currency, None)


@cache(timeout=5)
def calc_tax(price, rate=0.05):
    """計算含稅價格"""
    time.sleep(0.3)
    return round(price * (1 + rate), 2)


# ══════════════════════════════════════════════════════
#  主程式
# ══════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=== 查詢匯率（快取 3 秒）===")
    get_exchange_rate("USD")          # 重新計算
    get_exchange_rate("USD")          # 快取命中
    get_exchange_rate("JPY")          # 重新計算（不同參數）
    get_exchange_rate("JPY")          # 快取命中

    print("\n等待 4 秒，讓快取過期...")
    time.sleep(4)

    get_exchange_rate("USD")          # 快取過期，重新計算
    get_exchange_rate("USD")          # 快取命中

    print("\n=== 計算含稅價格（快取 5 秒）===")
    calc_tax(1000)                    # 重新計算
    calc_tax(1000)                    # 快取命中
    calc_tax(2000)                    # 重新計算（不同參數）
