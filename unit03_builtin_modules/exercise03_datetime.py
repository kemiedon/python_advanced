"""exercise03_datetime.py

練習 3：時間與檔名
"""

from datetime import datetime


def timestamped_filename(prefix):
    now = datetime.now()
    return f"{prefix}_{now.strftime('%Y%m%d_%H%M%S')}.txt"


def print_now():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    print_now()
    print("filename:", timestamped_filename("report"))
