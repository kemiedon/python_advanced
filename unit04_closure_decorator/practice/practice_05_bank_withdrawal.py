"""practice_02_bank_withdrawal.py

【練習 05】裝飾器 — 銀行提款限制

情境：
  ATM 提款時，系統要同時做兩件事：
    1. 每日限額檢查：單筆不能超過 $5000
    2. 餘額檢查：帳戶餘額要夠才能領

  兩個檢查邏輯分別寫成裝飾器，然後疊加套用在提款函式上。

提示：
  - 兩個裝飾器可以疊加：@check_balance 在上、@check_daily_limit 在下
  - 疊加時執行順序：由上而下包裝 → 由外而內執行
  - 帳戶餘額用 dict 模擬（方便在閉包/裝飾器裡修改）
"""

# 模擬帳戶資料
account = {
    "owner":   "小明",
    "balance": 8000,   # 目前餘額
}

DAILY_LIMIT = 5000     # 每日提款上限


# ── 裝飾器 1：每日限額檢查 ───────────────────────────────────
def check_daily_limit(func):
    def wrapper(amount):
        # TODO: 如果 amount > DAILY_LIMIT，印出拒絕訊息並 return
        ___
        return func(amount)
    return wrapper


# ── 裝飾器 2：餘額檢查 ───────────────────────────────────────
def check_balance(func):
    def wrapper(amount):
        # TODO: 如果 amount > account["balance"]，印出拒絕訊息並 return
        ___
        return func(amount)
    return wrapper


# ── 套用兩個裝飾器 ───────────────────────────────────────────
# 提示：@check_balance 在上（先檢查餘額），@check_daily_limit 在下（先檢查限額）
# 實際執行順序：check_balance → check_daily_limit → withdraw
@check_balance
@check_daily_limit
def withdraw(amount):
    """實際執行提款"""
    account["balance"] -= amount
    print(f"✅ 提款 ${amount} 成功！剩餘餘額：${account['balance']}")


# ══════════════════════════════════════════════════════
#  主程式
# ══════════════════════════════════════════════════════
if __name__ == "__main__":
    print(f"帳戶：{account['owner']}，目前餘額：${account['balance']}\n")

    withdraw(1000)   # ✅ 成功，餘額 7000
    withdraw(6000)   # ❌ 超過每日限額 $5000
    withdraw(7500)   # ❌ 超過每日限額（先被限額擋住）
    withdraw(3000)   # ✅ 成功，餘額 4000
    withdraw(4500)   # ❌ 餘額不足（剩 4000）
