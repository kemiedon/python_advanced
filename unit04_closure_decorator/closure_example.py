"""closure_example.py

示範：倍數產生器（閉包）
"""


def make_multiplier(factor):
    """
    這是一個外層函式，用來建立倍數產生器。
    """
    def multiplier(number):
        # multiplier 記住了 factor 這個來自外部作用域的變數
        return number * factor
    
    return multiplier

# 建立一個專門「翻 3 倍」的函式
triple_it = make_multiplier(3)

# 建立一個專門「翻 10 倍」的函式
deca_it = make_multiplier(10)

print(triple_it(5))  # 輸出 15
print(deca_it(5))    # 輸出 50