"""exercise02_math.py

練習 2：數學工具應用
"""

import math


def calc_hypotenuse(a, b):
    return math.hypot(a, b)


def angle_to_radian_and_back(deg):
    rad = math.radians(deg)
    return math.sin(rad), math.cos(rad)


if __name__ == "__main__":
    print("hypotenuse(3,4)=", calc_hypotenuse(3, 4))
    print("sin/cos(90)=", angle_to_radian_and_back(90))
