"""require_login_example.py

範例：門禁裝飾器（檢查權限）
"""


def require_login(func):
    def wrapper(user):
        if not user:
            print("❌ 請先登入")
            return
        print("✓ 已驗證身份，開始執行")
        func(user)

    return wrapper


@require_login
def access_system(user):
    print(f"歡迎 {user}，進入系統")


if __name__ == "__main__":
    access_system("小明")  # ✓ 已驗證身份，開始執行 / 歡迎 小明，進入系統
    access_system(None)  # ❌ 請先登入
