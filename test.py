def vip_required(func):
    """
    這是一個驗證海關：
    檢查使用者等級，如果不符合條件，直接攔截，不執行原函式。
    """
    def wrapper(user_info, *args, **kwargs):
        # 1. 執行固定判斷邏輯
        if user_info.get("level") != "VIP":
            return "❌ 錯誤：此功能僅限 VIP 會員使用！"
        
        # 2. 通過驗證，才放行執行原函式
        return func(user_info, *args, **kwargs)
        
    return wrapper

@vip_required
def generate_long_article(user_info, topic):
    return f"✨ [VIP 專屬] 已為您生成關於 {topic} 的 3000 字長文。"

# --- 測試情境 ---
user_a = {"name": "小明", "level": "Free"}
user_b = {"name": "老張", "level": "VIP"}

print(generate_long_article(user_a, "區塊鏈技術")) # 被攔截
print(generate_long_article(user_b, "區塊鏈技術")) # 成功執行