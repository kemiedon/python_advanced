"""example_datetime.py

示範 datetime 模組
"""

from datetime import datetime


def demo():
    now = datetime.now()
    print("now =", now)
    print("year,month,day =", now.year, now.month, now.day)
    print("formatted =", now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    demo()
