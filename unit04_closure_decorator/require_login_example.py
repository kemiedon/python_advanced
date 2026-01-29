"""require_login_example.py

範例：門禁裝飾器（檢查權限）
"""


def require_login(func):
    def wrapper(user, password):
        if not user:
            print("❌ 請先輸入帳號")
            return
        if password != "123456":
            print("❌ 密碼錯誤，請重新輸入")
            return
        print("✓ 已驗證身份，開始執行")
        func(user)

    return wrapper


@require_login
def access_system(user):
    print(f"歡迎 {user}，進入系統")


if __name__ == "__main__":
    # 示範互動式登入
    user = input("請輸入帳號：")
    password = input("請輸入密碼：")
    access_system(user, password)
