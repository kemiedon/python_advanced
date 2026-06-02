"""practice_04_decorator_validator.py

【練習 04】裝飾器 — KTV 年齡驗證 + 帶參數的裝飾器

情境：
  Part A — KTV 入場年齡驗證：
    進入 KTV 必須滿 18 歲，不然拒絕入場。
    用裝飾器自動幫每個操作進行年齡驗證，
    不用在每個操作裡重複寫。

  Part B — 帶參數的裝飾器：
    同樣的年齡限制邏輯，但不同場所門檻不同
    （KTV 18+、酒吧 21+）。
    用「帶參數的裝飾器」讓限制可以彈性設定。

提示：
  Part A — 標準裝飾器 = 2 層巢狀函式
  Part B — 帶參數的裝飾器 = 3 層巢狀函式
           @age_required(18)  →  age_required(18) 回傳一個裝飾器
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Part A：標準裝飾器（不帶參數）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def require_adult(func):
    """KTV 年齡門檻：滿 18 歲才能入場"""

    def wrapper(*args, **kwargs):
        # 約定：第一個參數是年齡
        if args:
            age = args[0]
            # TODO: 如果 age < 18，印出拒絕訊息並 return
            ___

        # TODO: 年齡合格則呼叫原始函式並回傳
        ___

    return wrapper


@require_adult
def enter_ktv(age, name):
    print(f"歡迎 {name}（年齡 {age}）入場，盡情盡興！")


@require_adult
def buy_alcohol(age, drink):
    print(f"已幫您上 {drink}，請慢用！")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Part B：帶參數的裝飾器（三層巢狀）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def age_required(min_age):
    """
    帶參數的裝飾器工廠，可彈性設定年齡門檻。
    使用方式：@age_required(18)
    """
    # 第二層：接收被裝飾的函式
    def decorator(func):
        # 第三層：包裝函式，執行年齡驗證
        def wrapper(*args, **kwargs):
            if args:
                age = args[0]
                # TODO: 如果 age < min_age，印出拒絕訊息並 return
                ___

            # TODO: 驗證通過則呼叫並回傳原始函式
            ___

        return wrapper
    return decorator


@age_required(18)
def enter_ktv_flex(age, name):
    print(f"歡迎 {name}（年齡 {age}）進入 KTV！")


@age_required(21)
def enter_bar(age, name):
    print(f"歡迎 {name}（年齡 {age}）進入酒吧！")


if __name__ == "__main__":
    print("=== Part A：標準裝飾器 ===")
    enter_ktv(20, "小明")   # 歡迎 小明（年齡 20）入場
    enter_ktv(16, "小華")   # 拒絕：16 歲未滿 18
    buy_alcohol(22, "啤酒")  # 已幫您上 啤酒
    buy_alcohol(17, "啤酒")  # 拒絕：17 歲未滿 18

    print("\n=== Part B：帶參數的裝飾器 ===")
    enter_ktv_flex(19, "小強")  # KTV 18+，通過
    enter_ktv_flex(15, "小安")  # KTV 18+，拒絕
    enter_bar(22, "大堂")       # 酒吧 21+，通過
    enter_bar(19, "小君")       # 酒吧 21+，拒絕
    print("  兩者本質相同，裝飾器是閉包的一種應用！")
