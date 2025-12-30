"""closure_example.py

示範：專屬筆記本（閉包）
"""


def make_counter(name):
    count = 0  # 外層變數

    def add_one():
        nonlocal count
        count += 1
        print(f"{name} 的計數：{count}")

    return add_one


if __name__ == "__main__":
    # 每位學生有自己的計數器
    小明計數 = make_counter("小明")
    小美計數 = make_counter("小美")

    小明計數()  # 輸出：小明 的計數：1
    小明計數()  # 輸出：小明 的計數：2
    小美計數()  # 輸出：小美 的計數：1
    小美計數()  # 輸出：小美 的計數：2
