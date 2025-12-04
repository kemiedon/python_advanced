"""timeit_example.py

範例：簡單的裝飾器（記錄執行時間）
"""

import time


def timeit(func):
    def wrapper():
        print(f"開始執行 {func.__name__}")
        start = time.time()
        func()
        end = time.time()
        print(f"執行時間：{end - start:.2f} 秒")

    return wrapper


@timeit
def slow_task():
    time.sleep(1)
    print("完成任務")


if __name__ == "__main__":
    slow_task()
