"""practice_03_decorator_logger.py

【練習 03】裝飾器 — 餐廳出菜記錄器

情境：
  餐廳送出任何一道菜後，都要在廚房日誌上印下
  「出菜了什麼、幾盤」，方便對帳。
  不想在每道菜的函式裡面一次次加 print，
  用裝飾器就能一勞永逸！

提示：
  - 裝飾器 = 一個「接收函式、回傳函式」的函式
  - @kitchen_log 等同於 serve_dish = kitchen_log(serve_dish)
  - *args, **kwargs 讓 wrapper 可以適用於任何函式
  - func.__name__ 可以取得被裝飾的函式名稱
"""


def kitchen_log(func):
    def wrapper(*args, **kwargs):
        # TODO: 印出廚房日誌（出菜哪道、傳入什麼參數）
        print(___)

        # TODO: 呼叫原始函式，存入 result
        result = ___

        # TODO: 印出出菜完成的訊息
        print(___)

        return result

    return wrapper


# 將裝飾器套用到首菜、主菜、甜點
@kitchen_log
def serve_appetizer(name, qty=1):
    print(f"  端上 {name} x{qty} 盤")
    return name


@kitchen_log
def serve_main(name, qty=1):
    print(f"  端上 {name} x{qty} 盤")
    return name


@kitchen_log
def serve_dessert(name):
    print(f"  端上 {name}")
    return name


if __name__ == "__main__":
    print("=== 桃桌 3 號開始上菜 ===")
    serve_appetizer("沙拉", qty=2)
    serve_main("牛排", qty=1)
    serve_dessert("布蕾")
    # 預期輸出範例：
    # [廚房日誌] serve_appetizer 被呼叫，參數: ('沙拉',) {'qty': 2}
    #   端上 沙拉 x2 盤
    # [廚房日誌] serve_appetizer 完成，回傳: 沙拉
