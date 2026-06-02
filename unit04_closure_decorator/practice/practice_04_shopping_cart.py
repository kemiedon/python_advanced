"""practice_01_shopping_cart.py

【練習 04】閉包 — 購物車

情境：
  網路購物時，每位顧客都有自己的購物車。
  購物車要能「加商品」、「移除商品」、「查看總額」，
  而且不同顧客的購物車完全獨立，不互相影響。

提示：
  - 外層函式建立購物車（dict 存商品與價格）
  - 回傳「三個內層函式」包在 dict 裡，讓外部可以呼叫
  - 內層函式共享同一份 cart（這就是閉包的作用）
  - 不需要 nonlocal（因為我們是修改 dict 內容，不是重新賦值）

回傳格式：
  {
      "add":    加入商品的函式,
      "remove": 移除商品的函式,
      "total":  查看總額的函式,
  }
"""


def make_cart(owner):
    """
    owner: 顧客名稱（str）
    建立一個屬於 owner 的購物車，回傳操作函式的 dict
    """
    # TODO: 建立一個空 dict 存放商品，格式 {商品名: 價格}
    cart = ___

    def add(item, price):
        """加入商品"""
        # TODO: 把 item 與 price 存入 cart
        ___
        print(f"[{owner}的購物車] 加入 {item}（${price}）")

    def remove(item):
        """移除商品"""
        # TODO: 如果 item 在 cart 裡就移除，否則印出「找不到商品」
        if ___:
            ___
            print(f"[{owner}的購物車] 移除 {item}")
        else:
            print(f"[{owner}的購物車] 找不到 {item}")

    def total():
        """查看目前購物車總額"""
        # TODO: 計算 cart 裡所有商品價格的總和
        amount = ___
        print(f"[{owner}的購物車] 目前商品：{list(cart.keys())}，總計 ${amount}")
        return amount

    # 回傳三個操作函式
    return {"add": add, "remove": remove, "total": total}


# ══════════════════════════════════════════════════════
#  主程式
# ══════════════════════════════════════════════════════
if __name__ == "__main__":
    # 建立兩位顧客的購物車
    alice = make_cart("Alice")
    bob   = make_cart("Bob")

    print("=== Alice 購物 ===")
    alice["add"]("蘋果", 50)
    alice["add"]("牛奶", 80)
    alice["add"]("麵包", 40)
    alice["total"]()         # 總計 $170

    print("\n=== Bob 購物 ===")
    bob["add"]("咖啡", 120)
    bob["add"]("餅乾", 60)
    bob["total"]()           # 總計 $180

    print("\n=== Alice 移除商品 ===")
    alice["remove"]("牛奶")
    alice["remove"]("果汁")  # 找不到
    alice["total"]()         # 總計 $90

    print("\n=== 驗證互不影響 ===")
    bob["total"]()           # Bob 應仍是 $180，不受 Alice 影響
