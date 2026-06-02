"""practice_01_closure_counter.py

【練習 01】閉包 — 自動販賣機

情境：
  便利商店裡的自動販賣機，每按一次按鈕就賣出一罐飲料，
  並顯示「已賣出幾罐」。
  不同的販賣機要各自計算，互不影響。

提示：
  - 閉包讓內層函式可以「記住」外層函式的變數
  - 修改外層變數時要加 nonlocal
  - 回傳函式時不加括號：return sell（不是 return sell()）
"""


def make_vending_machine():
    # TODO: 宣告一個變數記錄賣出數量，初始為 0
    sold = ___

    def sell():
        # TODO: 用 nonlocal 宣告 sold
        ___
        # TODO: sold 加 1，並印出「已賣出 X 罐」
        ___
        ___

    return sell


if __name__ == "__main__":
    machine_a = make_vending_machine()  # 7-11 的販賣機
    machine_b = make_vending_machine()  # 全家的販賣機

    machine_a()  # 已賣出 1 罐
    machine_a()  # 已賣出 2 罐
    machine_b()  # 已賣出 1 罐  ← 和 machine_a 互不影響
    machine_a()  # 已賣出 3 罐"
