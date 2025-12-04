# 單元 1 練習 2：類別屬性設計（難度：⭐⭐）
# 設計一個「洗衣機」類別來表示不同的洗衣機型號


class WashingMachine:
    def __init__(self, brand, capacity):
        """
        初始化洗衣機的基本資訊
        :param brand: 品牌名稱
        :param capacity: 容量（公斤）
        """
        self.brand = brand
        self.capacity = capacity

    def display_info(self):
        """顯示洗衣機的品牌和容量"""
        print(f"品牌：{self.brand}，容量：{self.capacity} 公斤")


if __name__ == "__main__":
    # 建立兩個不同品牌的洗衣機實例
    machine1 = WashingMachine("LG", 8)
    machine2 = WashingMachine("三星", 10)

    # 顯示洗衣機資訊
    machine1.display_info()
    machine2.display_info()
