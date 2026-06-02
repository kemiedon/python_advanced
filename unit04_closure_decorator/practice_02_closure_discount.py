"""practice_02_closure_discount.py

【練習 02】閉包 — 超市結帳

情境：
  超市針對不同會員給予不同折扣：
    - 一般會員：九折（0.9）
    - VIP 會員：八折（0.8）
    - 黑金會員：七折（0.7）

  用「函式工廠」的方式，讓同一段程式碼產生不同的折扣函式。

提示：
  - 外層函式接收折扣率並「記住」它
  - 內層函式接收原價，用外層記住的折扣率來計算
"""


def make_discount(rate):
    # rate 會被內層函式「記住」

    def apply_discount(price):
        # TODO: 計算折扣後的金額（price × rate），存入 discounted
        discounted = ___
        # TODO: 印出「原價 X → 折扣後 Y」
        print(___)
        return discounted

    # TODO: 回傳內層函式
    return ___


if __name__ == "__main__":
    normal = make_discount(0.9)  # 一般會員
    vip    = make_discount(0.8)  # VIP
    gold   = make_discount(0.7)  # 黑金

    normal(1000)  # 原價 1000 → 折扣後 900
    vip(1000)     # 原價 1000 → 折扣後 800
    gold(1000)    # 原價 1000 → 折扣後 700
    normal(500)   # 原價 500  → 折扣後 450"
